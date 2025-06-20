import operator

from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Button, Start, Cancel, Select, Back, Column, ScrollingGroup
from aiogram_dialog.widgets.text import Const, Format, Case

from .states import SongState
from .getters import get_categories, get_songs, get_song
from .selects import select_category, back_category, select_song, back_song

category_choice = Window(
    Format('{current_song_category_title}'),
    Column(
        Select(
            Format('{item[name]}'),
            id='categories_s',
            items='data',
            item_id_getter=operator.itemgetter('id'),
            on_click=select_category
        )
    ),

    Button(
        Const('<< Назад'),
        on_click=back_category,
        id='back'
    ),
    Cancel(
        Const('<<< В главное меню')
    ),

    state=SongState.category_choice,
    getter=get_categories,
)

song_choice = Window(

    Case(
        {
            True: Const('Выбор песни'),
            False: Const('Песни в данной категории отсутствуют')
        },
        selector='available'
    ),
    ScrollingGroup(
        Column(
            Select(
                Format('{item[title]}'),
                id='songs_s',
                items='data',
                item_id_getter=operator.itemgetter('id'),
                on_click=select_song
            )
        ),
        id='scrl_song',
        height=10,
        hide_on_single_page=True,
    ),

    Button(
        Const('<< Назад'),
        on_click=back_category,
        id='back'
    ),
    Cancel(
        Const('<<< В главное меню')
    ),

    state=SongState.song_choice,
    getter=get_songs
)

song_view = Window(
    Format('<b>{song[title]}</b>\n'),
    Format('{song[text]}'),

    Button(
        Const('<< Назад'),
        on_click=back_song,
        id='back'
    ),

    parse_mode='HTML',
    getter=get_song,
    state=SongState.song_view
)