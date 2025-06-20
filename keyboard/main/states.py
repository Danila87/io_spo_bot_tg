from aiogram.filters.state import StatesGroup, State

class MainState(StatesGroup):
    main = State()
    about_pipif = State()
    additional = State()
    send_review = State()
    success = State()