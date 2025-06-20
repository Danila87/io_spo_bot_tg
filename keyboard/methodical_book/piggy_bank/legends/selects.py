from typing import Any

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager

from .states import Legends

from keyboard.search.states import SearchState

async def select_legend(
        callback: CallbackQuery,
        widget: Any,
        dialog_manager: DialogManager,
        item_id: int
):
    ctx = dialog_manager.current_context()
    ctx.dialog_data.update(legend_id=int(item_id))

    await dialog_manager.switch_to(Legends.legend_view)

async def legend_back(
        callback: CallbackQuery,
        widget: Any,
        dialog_manager: DialogManager,
):
    ctx = dialog_manager.current_context()

    if 'search_items' in ctx.start_data:
        await dialog_manager.start(SearchState.search_result, data={
            'search_items': ctx.start_data.get('search_items')
        })
    else:
        await dialog_manager.back()