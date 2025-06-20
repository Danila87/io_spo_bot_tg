from aiogram_dialog import Dialog
from .windows import search_result_window, input_title_window

search_dialog = Dialog(
    input_title_window,
    search_result_window
)