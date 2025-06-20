from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Start, Button, SwitchTo, Back, Next
from aiogram_dialog.widgets.text import Const, Case, Format
from aiogram_dialog.widgets.input import TextInput

from .states import MainState
from .getters import create_review, get_about_pipif

from keyboard.song.states import SongState
from keyboard.methodical_book.states import MethodicalBook
from keyboard.search.states import SearchState
from keyboard.statistic.states import StatisticState

main_window = Window(
    Const('Главное меню'),
    Start(Const('Поиск 🔎'), id='search', state=SearchState.input_title),
    Start(Const('Песни 🎵'), id='songs', state=SongState.category_choice),
    Start(Const('Методичка 📁'), id='methodical_book', state=MethodicalBook.main),
    Start(Const('Статистика 📊'), id='statistic', state=StatisticState.choice_dashboard),
    SwitchTo(Const('Дополнительно ℹ️'), id='additional_info', state=MainState.additional),
    state=MainState.main
)

additional_window = Window(
    Const('Дополнительно'),
    SwitchTo(Const('Что такое Pipif? 🦊'), id='about_pipif', state=MainState.about_pipif),
    SwitchTo(Const('Оставить отзыв 💬'), id='send_review', state=MainState.send_review),
    SwitchTo(Const('<< Назад'), id='back', state=MainState.main),
    state=MainState.additional
)

about_pipif_window = Window(
    Format('{text}'),
    SwitchTo(Const('<< Назад'), id='back', state=MainState.additional),
    getter=get_about_pipif,
    state=MainState.about_pipif
)

send_review_window = Window(
    Const('Напишите отзыв следующим сообщением'),
    TextInput(id="send_review", on_success=Next()),
    state=MainState.send_review
)

success_window = Window(
    Case(
        texts={
            True: Const('Отзыв успешно отправлен'),
            False: Const('Произошла ошибка при отправке отзыва, попробуйте позже')
        },
        selector='success'
    ),
    SwitchTo(Const('<< Назад'), id='back', state=MainState.additional),
    getter=create_review,
    state=MainState.success
)