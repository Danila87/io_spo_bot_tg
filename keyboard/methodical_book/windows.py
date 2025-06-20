from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Button, Start, Cancel, Back
from aiogram_dialog.widgets.text import Const

from .states import MethodicalBook
from .methodical.states import Methodical

from keyboard.main.states import MainState

from .piggy_bank.states import PiggyBank


main_window = Window(
    Const('Выбор раздела'),
    Start(Const('Метод папка'), id='methodical', state=Methodical.main_view),
    Start(Const('Копилка'), id='piggy_bank', state=PiggyBank.children_group_choice),
    Start(Const('<< Назад'), id='back', state=MainState.main),
    state=MethodicalBook.main,
)

