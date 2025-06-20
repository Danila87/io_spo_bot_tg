import operator

from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Start, Column, Select, Back, Cancel, Button, ScrollingGroup
from aiogram_dialog.widgets.media import DynamicMedia
from aiogram_dialog.widgets.text import Const, Format, Case

from keyboard.main.states import MainState

from .states import Legends
from .selects import select_legend, legend_back
from .getters import get_legends, get_legend

legend_choice = Window(
    Case(
        {
            True: Const('Выбор легенды'),
            False: Const('В данной категории детей отсутствуют легенды')
        },
        selector='available'
    ),
    ScrollingGroup(
        Column(
            Select(
                Format('{item[title]}'),
                id='legend_choice',
                item_id_getter=operator.itemgetter('id'),
                items='data',
                on_click=select_legend
        )
    ),
        height=5,
        width=1,
        hide_on_single_page=True,
        id='scrl_legend'
    ),

    Cancel(Const('<< Назад')),
    Start(Const('<<< В главное меню'), id='back_to_main', state=MainState.main),
    state=Legends.legend_choice,
    getter=get_legends
)

legend_view = Window(
    Format('{data[title]}'),
    Format('{data[description]}'),
    DynamicMedia('file'),
    Button(Const('<< Назад'), id='back', on_click=legend_back),
    state=Legends.legend_view,
    getter=get_legend
)