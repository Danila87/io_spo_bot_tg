from typing import Any

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager

from keyboard.methodical_book.piggy_bank.games.states import Games
from keyboard.methodical_book.piggy_bank.legends.states import Legends
from keyboard.methodical_book.piggy_bank.ktd.states import KTD
from keyboard.song.states import SongState

from keyboard.search.states import SearchState

async def select_item(
        callback: CallbackQuery,
        widget: Any,
        dialog_manager: DialogManager,
        item_id: int
):
    ctx = dialog_manager.current_context()

    select_mapping = {
        'song_s': SongState.song_view,
        'game_s': Games.game_view,
        'ktd_s': KTD.ktd_view,
        'legend_s': Legends.legend_view
    }

    state = select_mapping.get(
        widget.widget_id
    )

    data = {
        'search_id': item_id,
        'search_items': ctx.dialog_data.get('search_items')
    }

    await dialog_manager.start(state, data=data)

async def back_search(
        callback: CallbackQuery,
        widget: Any,
        dialog_manager: DialogManager,
):
    ctx = dialog_manager.current_context()
    ctx.start_data = None

    await dialog_manager.back()
