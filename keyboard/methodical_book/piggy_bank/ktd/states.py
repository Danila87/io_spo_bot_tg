from aiogram.filters.state import StatesGroup, State

class KTD(StatesGroup):
    ktd_choice = State()
    ktd_view = State()