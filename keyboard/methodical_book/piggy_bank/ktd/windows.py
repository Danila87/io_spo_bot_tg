import operator

from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Column, Select, Back, Cancel, Start, Button, ScrollingGroup
from aiogram_dialog.widgets.media import DynamicMedia
from aiogram_dialog.widgets.text import Const, Format, Case

from keyboard.main.states import MainState

from .getters import get_ktds, get_ktd
from .selects import ktd_select, ktd_back
from .states import KTD

ktd_choice = Window(
    Case(
        {
            True: Const('Выбор КТД'),
            False: Const('В данной категории детей отсутствуют КТД')
        },
        selector='available'
    ),

    ScrollingGroup(
        Column(
            Select(
                Format('{item[title]}'),
                id='ktd_choice',
                item_id_getter=operator.itemgetter('id'),
                items='data',
                on_click=ktd_select
            )
        ),
        id='scrl_ktd',
        height=5,
        width=1,
        hide_on_single_page=True
    ),

    Cancel(Const('<< Назад')),
    Start(Const('<<< В главное меню'), id='back_to_main', state=MainState.main),
    state=KTD.ktd_choice,
    getter=get_ktds
)

ktd_view = Window(
    Format('{data[title]}'),
    Format('{data[description]}'),
    DynamicMedia('file'),
    Button(Const('<< Назад'), id='back', on_click=ktd_back),
    state=KTD.ktd_view,
    getter=get_ktd
)