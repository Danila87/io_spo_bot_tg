from aiogram_dialog import Dialog
from keyboard.statistic.windows import dashboard_choice, visualisation_choice, visualisation_view

statistic_dialog = Dialog(
    dashboard_choice,
    visualisation_choice,
    visualisation_view
)