from aiogram_dialog import Dialog
from .windows import category_choice, song_choice, song_view

song_dialog = Dialog(
    category_choice,
    song_choice,
    song_view
)