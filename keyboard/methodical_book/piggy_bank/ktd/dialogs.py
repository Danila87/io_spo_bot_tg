from aiogram_dialog import Dialog
from .windows import ktd_choice, ktd_view

ktd_dialog = Dialog(
    ktd_choice,
    ktd_view
)