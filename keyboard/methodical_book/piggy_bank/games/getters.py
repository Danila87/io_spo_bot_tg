from datetime import datetime
from pathlib import Path

from aiogram_dialog import DialogManager
from aiogram_dialog.api.entities import MediaAttachment

from common_lib.api_client.client import api_client, url_f
from common_lib.utils import get_file_content_type, save_file
from common_lib.redis.redis_client import cache_data_file
from schemas.dto import DTOWithFile


async def get_types(
        dialog_manager: DialogManager,
        **kwargs
):
    types = await api_client.call_async_get(
        url=url_f.game_types
    )

    return {
        'count': len(types),
        'data': types
    }

async def get_games(
        dialog_manager: DialogManager,
        **kwargs
):
    ctx = dialog_manager.current_context()
    group_id = ctx.start_data.get('children_group_id')
    type_id = ctx.dialog_data.get('game_type_id')

    games = await api_client.call_async_get(
        url=url_f.games_by_type_group,
        params={
            'type_id': type_id,
            'group_id': group_id
        }
    )

    return {
        'count': len(games),
        'data': games,
        'available': True if games else False
    }

@cache_data_file(expire=21600)
async def get_game(
        dialog_manager: DialogManager,
        **kwargs
) -> DTOWithFile:
    ctx = dialog_manager.current_context()

    if start_data := ctx.start_data:
        game_id = start_data.get('search_id', ctx.dialog_data.get('game_id'))
    else:
        game_id = ctx.dialog_data.get('game_id')

    game = await api_client.call_async_get(
        url=url_f.games,
        params={
            'game_id': game_id
        }
    )

    if (file_data := await api_client.get_file(
            url=url_f.game_file,
            params={
                'game_id': game_id
            }
        )) is None:
        return DTOWithFile(
        data=game,
        file_path=None,
        file=None
    )

    if file_data.filename is None:
        file_data.filename = f'{datetime.now().isoformat()}{file_data.file_type}'

    if not (file := Path('temp', file_data.filename)).exists():
        file = await save_file(
            file_data=file_data
        )

    content_type = get_file_content_type(file.suffix)

    file_media = MediaAttachment(type=content_type, path=str(file.resolve()))

    return DTOWithFile(
        data=game,
        file_path=str(file.resolve()),
        file=file_media
    )