from aiogram_dialog import DialogManager

from common_lib.api_client.client import api_client, url_f
from common_lib.redis.redis_client import cache_data_file
from common_lib.utils import save_file, get_file_content_type
from aiogram_dialog.api.entities import MediaAttachment
from pathlib import Path

from schemas.dto import DTOWithFile


async def get_ktds(
        dialog_manager: DialogManager,
        **kwargs
):
    ctx = dialog_manager.current_context()
    group_id = ctx.start_data.get('children_group_id')

    ktds = await api_client.call_async_get(
        url=url_f.ktds_by_group,
        params={
            'group_id': group_id
        }
    )

    return {
        'count': len(ktds),
        'data': ktds,
        'available': True if ktds else False
    }

@cache_data_file(expire=21600)
async def get_ktd(
        dialog_manager: DialogManager,
        **kwargs
) -> DTOWithFile:
    ctx = dialog_manager.current_context()

    if start_data := ctx.start_data:
        ktd_id = start_data.get('search_id', ctx.dialog_data.get('ktd_id'))
    else:
        ktd_id = ctx.dialog_data.get('ktd_id')

    ktd = await api_client.call_async_get(
        url=url_f.ktd_by_id,
        params={
            'ktd_id': ktd_id
        }
    )

    if (file_data := await api_client.get_file(
            url=url_f.ktd_file,
            params={
                'ktd_id': ktd_id
            }
        )) is None:

        return DTOWithFile(
        data=ktd,
        file_path=None,
        file=None
    )

    if not (file := Path('temp', file_data.filename)).exists():
        file = await save_file(
            file_data=file_data
        )

    content_type = get_file_content_type(file.suffix)

    file_media = MediaAttachment(type=content_type, path=str(file.resolve()))

    return DTOWithFile(
        data=ktd,
        file_path=str(file.resolve()),
        file=file_media
    )

