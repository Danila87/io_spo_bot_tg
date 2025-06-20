import operator

from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Button, Start, Column, Select, Cancel
from aiogram_dialog.widgets.media import DynamicMedia
from aiogram_dialog.widgets.text import Const, Format, Case

from .getters import get_chapters
from .selects import select_chapter, back_chapter
from .states import Methodical
from ...main.states import MainState

main_view = Window(
    Case(
        texts={
            True: Format('{current_chapter_title}'),
            False: Const('Подразделы и прилагаемые файлы к главе отсутствуют')
        },
        selector='available'
    ),
    Column(
            Select(
                Format('{item[title]}'),
                id='chapters_s',
                items='data',
                item_id_getter=operator.itemgetter('id'),
                on_click=select_chapter
            )
        ),
    Button(Const('<< Назад'), id='back', on_click=back_chapter),
    Start(Const('<<< В главное меню'), state=MainState.main, id='main_menu'),
    DynamicMedia('file'),
    state=Methodical.main_view,
    getter=get_chapters
)
