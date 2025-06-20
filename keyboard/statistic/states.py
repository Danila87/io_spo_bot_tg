from aiogram.filters.state import StatesGroup, State

class StatisticState(StatesGroup):
    choice_dashboard = State()
    choice_visualisation = State()
    visualisation_view = State()