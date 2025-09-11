from typing import Dict

from aiogram_dialog import DialogManager
from common_lib.api_client.client import api_client, url_f

async def get_children_groups(
        dialog_manager: DialogManager,
        **kwargs
) -> Dict:
    response = await api_client.call_async_get(
        url=url_f.piggy_bank_groups
    )

    return {
        'count': response['meta']['total'],
        'data': response['data'],
    }
