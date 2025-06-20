from typing import Any

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager

from keyboard.methodical_book.piggy_bank.games.states import Games
from keyboard.methodical_book.piggy_bank.legends.states import Legends
from keyboard.methodical_book.piggy_bank.ktd.states import KTD

async def select_children_group(
        callback: CallbackQuery,
        widget: Any,
        dialog_manager: DialogManager,
        item_id: int
):
    ctx = dialog_manager.current_context()
    ctx.dialog_data.update(children_group=int(item_id))

    await dialog_manager.next()

async def select_chapter(
        callback: CallbackQuery,
        widget: Any,
        dialog_manager: DialogManager,
):
    ctx = dialog_manager.current_context()
    group_id = ctx.dialog_data.get('children_group')
    data = {
        'children_group_id': group_id
    }

    if widget.widget_id == 'games':
        await dialog_manager.start(Games.type_game_choice, data=data)
    elif widget.widget_id == 'legends':
        await dialog_manager.start(Legends.legend_choice, data=data)
    elif widget.widget_id == 'ktd':
        await dialog_manager.start(KTD.ktd_choice, data=data)