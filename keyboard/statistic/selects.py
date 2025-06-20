from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager

from keyboard.statistic.states import StatisticState

from typing import Any

async def select_dashboard(
        callback: CallbackQuery,
        widget: Any,
        dialog_manager: DialogManager,
        item_id: int
):
    ctx = dialog_manager.current_context()
    ctx.dialog_data.update(dashboard_uid=item_id)

    await dialog_manager.switch_to(StatisticState.choice_visualisation)

async def select_visualisation(
        callback: CallbackQuery,
        widget: Any,
        dialog_manager: DialogManager,
        item_id: int
):
    ctx = dialog_manager.current_context()
    ctx.dialog_data.update(visualisation_id=item_id)

    await dialog_manager.switch_to(StatisticState.visualisation_view)