from aiogram_dialog import DialogManager

from common_lib.api_client.client import api_client, url_f
from common_lib.redis.redis_client import cache_data_file
from common_lib.utils import save_file, get_file_content_type
from aiogram_dialog.api.entities import MediaAttachment
from pathlib import Path

from schemas.dto import DTOWithFile


async def get_legends(
        dialog_manager: DialogManager,
        **kwargs
):
    ctx = dialog_manager.current_context()
    group_id = ctx.start_data.get('children_group_id')

    legends = await api_client.call_async_get(
        url=url_f.legends_by_group,
        params={
            'group_id': group_id
        }
    )

    return {
        'count': len(legends),
        'data': legends,
        'available': True if legends else False
    }

@cache_data_file(expire=21600)
async def get_legend(
        dialog_manager: DialogManager,
        **kwargs
):
    ctx = dialog_manager.current_context()

    if start_data := ctx.start_data:
        legend_id = start_data.get('search_id', ctx.dialog_data.get('legend_id'))
    else:
        legend_id = ctx.dialog_data.get('legend_id')

    legend = await api_client.call_async_get(
        url=url_f.legend_by_id,
        params={
            'legend_id': legend_id
        }
    )

    if (file_data := await api_client.get_file(
            url=url_f.legend_file,
            params={
                'legend_id': legend_id
            }
        )) is None:
        return DTOWithFile(
            data=legend,
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
        data=legend,
        file_path=str(file.resolve()),
        file=file_media
    )