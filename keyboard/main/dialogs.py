from aiogram_dialog import Dialog
from keyboard.main.windows import main_window, additional_window, about_pipif_window, send_review_window, success_window

main_dialog = Dialog(
    main_window,
    additional_window,
    about_pipif_window,
    send_review_window,
    success_window
)