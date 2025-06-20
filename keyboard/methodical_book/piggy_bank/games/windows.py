import operator

from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import ScrollingGroup, Select, Back, Cancel, Start, Button
from aiogram_dialog.widgets.media import DynamicMedia
from aiogram_dialog.widgets.text import Const, Format, Case

from keyboard.main.states import MainState

from .states import Games
from .getters import get_types, get_games, get_game
from .selects import game_type_select, game_select, game_back

game_type_choice = Window(
    Const('Выбор типа игры'),
    ScrollingGroup(
        Select(
            Format('{item[title]}'),
            id='game_type_choice',
            item_id_getter=operator.itemgetter('id'),
            items='data',
            on_click=game_type_select
        ),
        id='game_types_sg',
        width=2,
        height=5,
        hide_on_single_page=True
    ),
    Cancel(Const('<< Назад')),
    Start(Const('<<< В главное меню'), id='back_to_main', state=MainState.main),
    getter=get_types,
    state=Games.type_game_choice
)

game_choice = Window(
    Case(
        {
            True: Const('Выбор игры'),
            False: Const('Игры в данной группе и категории отсутствуют')
        },
        selector='available'
    ),

    ScrollingGroup(
                Select(
                Format('{item[title]}'),
                    id='game_choice',
                    item_id_getter=operator.itemgetter('id'),
                    items='data',
                    on_click=game_select
                ),
                id='games_sg',
        width=1,
                height=10,
                hide_on_single_page=True
            ),

    Back(Const('<< Назад'), id='back'),
    Start(Const('<<< В главное меню'), id='back_to_main', state=MainState.main),
    getter=get_games,
    state=Games.game_choice
)

game_show = Window(
    Format('{data[title]}'),
    Format('{data[description]}'),
    DynamicMedia('file'),
    Button(Const('<< Назад'), id='back', on_click=game_back),
    state=Games.game_view,
    getter=get_game
)