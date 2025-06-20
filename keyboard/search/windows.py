import operator
from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Start, Button, Column, Select, Group, Cancel, Next, Back, SwitchTo, \
    ScrollingGroup
from aiogram_dialog.widgets.text import Const, Format, Case
from aiogram_dialog.widgets.input import TextInput

from keyboard.main.states import MainState

from .states import SearchState
from .getters import get_search_data
from .selects import select_item, back_search

input_title_window = Window(
    Const('Введите ключевое слово для поиска'),
    Start(Const('<< Назад'), id='back_main_menu', state=MainState.main),
    TextInput(id='search_title', on_success=Next()),
    state=SearchState.input_title
)

search_result_window = Window(
    Case(
        {
            True: Const('Все что мне удалось найти'),
            False: Const('Я ничего не смог найти')
        },
        selector='available'
    ),

    ScrollingGroup(
                Select(
                    Format('{item[title]} (Песня)'),
                    id='song_s',
                    item_id_getter=operator.itemgetter('id'),
                    items='songs',
                    on_click=select_item
                ),
                Select(
                    Format('{item[title]} (Игра)'),
                    id='game_s',
                    item_id_getter=operator.itemgetter('id'),
                    items='games',
                    on_click=select_item
                ),
                Select(
                    Format('{item[title]} (Легенда)'),
                    id='legend_s',
                    item_id_getter=operator.itemgetter('id'),
                    items='legends',
                    on_click=select_item
                ),
                Select(
                    Format('{item[title]} (КТД)'),
                    id='ktd_s',
                    item_id_getter=operator.itemgetter('id'),
                    items='ktds',
                    on_click=select_item
                ),
        id='scroll_group',
        height=10,
        width=1,
        hide_on_single_page=True
    ),

#     Group(
#         Select(
#             Format('{item[title]} (Песня)'),
#             id='song_s',
#             item_id_getter=operator.itemgetter('id'),
#             items='songs',
#             on_click=select_item
#         ),
#         width=1
#     ),
#     Group(
#         Select(
#             Format('{item[title]} (Игра)'),
#             id='game_s',
#             item_id_getter=operator.itemgetter('id'),
#             items='games',
#             on_click=select_item
#         ),
# width=1
#     ),
#     Group(
#         Select(
#             Format('{item[title]} (Легенда)'),
#             id='legend_s',
#             item_id_getter=operator.itemgetter('id'),
#             items='legends',
#             on_click=select_item
#         ),
# width=1
#     ),
#
#     Group(
#         Select(
#             Format('{item[title]} (КТД)'),
#             id='ktd_s',
#             item_id_getter=operator.itemgetter('id'),
#             items='ktds',
#             on_click=select_item
#         ),
# width=1
#     ),

    Button(Const('<< Назад'), on_click=back_search, id='back'),

    getter=get_search_data,
    state=SearchState.search_result,
)

