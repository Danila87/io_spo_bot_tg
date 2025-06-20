from aiogram.filters.state import StatesGroup, State

class SearchState(StatesGroup):
    input_title = State()
    search_result = State()