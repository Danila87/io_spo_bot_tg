from aiogram.filters.state import StatesGroup, State

class Games(StatesGroup):
    type_game_choice = State()
    game_choice = State()
    game_view = State()