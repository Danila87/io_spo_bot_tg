from datetime import datetime
from pathlib import Path

from aiogram_dialog import DialogManager
from aiogram_dialog.api.entities import MediaAttachment

from common_lib.api_client.client import api_client, url_f
from common_lib.utils import get_file_content_type, save_file
from common_lib.redis.redis_client import cache_data_file
from schemas.dto import DTOWithFile


async def get_dashboards(
        dialog_manager: DialogManager,
        **kwargs
):
    available = False

    if dashboards := await api_client.call_async_get(
        url=url_f.bot_dashboards
    ):
        available = True

    return {
        'dashboards': dashboards,
        'available': available
    }

async def get_visualisations(
        dialog_manager: DialogManager,
        **kwargs
):
    available = False

    ctx = dialog_manager.current_context()
    dashboard_uid = ctx.dialog_data.get('dashboard_uid')

    if visualisations := await api_client.call_async_get(
            url=url_f.visualisation(
                dashboard_uid=dashboard_uid
            )
    ):
        available = True

    return {
        'visualisations': visualisations,
        'available': available
    }

@cache_data_file(
    expire=21600
)
async def get_visualisation(
        dialog_manager: DialogManager,
        **kwargs
) -> DTOWithFile:
    ctx = dialog_manager.current_context()

    visualisation = await api_client.get_file(
        url=url_f.visualisation_imp(
            dashboard_uid=ctx.dialog_data.get('dashboard_uid'),
            visualisation_id=ctx.dialog_data.get('visualisation_id')
        )
    )

    if visualisation.filename is None:
        visualisation.filename = f'{datetime.now().isoformat()}{visualisation.file_type}'

    if not (file := Path('temp', visualisation.filename)).exists():
        file = await save_file(
            file_data=visualisation
        )

    content_type = get_file_content_type(file.suffix)

    file_media = MediaAttachment(type=content_type, path=str(file.resolve()))

    return DTOWithFile(
        file_path=str(file.resolve()),
        file=file_media
    )
