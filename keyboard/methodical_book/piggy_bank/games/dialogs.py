from aiogram_dialog import Dialog
from .windows import game_type_choice, game_choice, game_show

games_dialog = Dialog(
    game_type_choice,
    game_choice,
    game_show
)