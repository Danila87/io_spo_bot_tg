from aiogram.filters.state import StatesGroup, State

class PiggyBank(StatesGroup):
    children_group_choice = State()
    chapters_choice = State()
