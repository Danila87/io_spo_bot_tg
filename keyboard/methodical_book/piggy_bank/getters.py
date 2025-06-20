from typing import Dict

from aiogram_dialog import DialogManager
from common_lib.api_client.client import api_client, url_f

async def get_children_groups(
        dialog_manager: DialogManager,
        **kwargs
) -> Dict:

    if children_groups := await api_client.call_async_get(
        url=url_f.children_groups
    ):
        return {
            'count': len(children_groups),
            'data': children_groups
        }
