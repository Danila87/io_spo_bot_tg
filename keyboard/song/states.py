from aiogram.filters.state import StatesGroup, State

class SongState(StatesGroup):
    category_choice = State()
    song_choice = State()
    song_view = State()
