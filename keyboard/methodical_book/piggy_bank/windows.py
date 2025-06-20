import operator

from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Button, Start, Cancel, Back, Column, Select
from aiogram_dialog.widgets.text import Const, Format

from .getters import get_children_groups
from .states import PiggyBank
from .selects import select_children_group, select_chapter

from keyboard.main.states import MainState

children_groups_choice = Window(
    Const('Выбор возраста'),

    Column(
        Select(
            Format('{item[title]}'),
            id='children_groups_s',
            items='data',
            item_id_getter=operator.itemgetter('id'),
            on_click=select_children_group
        )
    ),

    Cancel(Const('<< Назад')),
    Start(Const('<<< В главное меню'), id='back_to_main', state=MainState.main),
    state=PiggyBank.children_group_choice,
    getter=get_children_groups
)

piggy_bank_chapters_choice = Window(
    Const('Выбор раздела'),
    Button(Const('Игры'), id='games', on_click=select_chapter),
    Button(Const('Легенды'), id='legends', on_click=select_chapter),
    Button(Const('КТД'), id='ktd', on_click=select_chapter),
    Back(Const('<< Назад')),
    Start(Const('<<< В главное меню'), id='back_to_main', state=MainState.main),

    state=PiggyBank.chapters_choice,
)

