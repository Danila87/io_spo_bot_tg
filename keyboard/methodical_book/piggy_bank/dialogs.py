from aiogram_dialog import Dialog
from .windows import children_groups_choice, piggy_bank_chapters_choice

piggy_bank_dialog = Dialog(
    children_groups_choice,
    piggy_bank_chapters_choice
)