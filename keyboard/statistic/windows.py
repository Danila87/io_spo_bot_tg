import operator

from aiogram.enums import ParseMode
from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Start, Button, SwitchTo, Back, Next, Column, Select, Cancel
from aiogram_dialog.widgets.media import DynamicMedia
from aiogram_dialog.widgets.text import Const, Case, Format

from .states import StatisticState
from .getters import get_dashboards, get_visualisations, get_visualisation
from .selects import select_dashboard, select_visualisation

dashboard_choice = Window(
    Const('Выбор дашборда'),
                Column(
                        Select(
                            Format('{item[title]}'),
                            id='dashboard_s',
                            items='dashboards',
                            item_id_getter=operator.itemgetter('uid'),
                            on_click=select_dashboard
                        )
                    ),
    Cancel(Const('<< Назад'), id='back'),
    getter=get_dashboards,
    state=StatisticState.choice_dashboard
)

visualisation_choice = Window(
    Const('Выбор статистики\n⚠️ <em>Статистика может загружаться до 30 сек. !</em> ⚠️'),
                Column(
                        Select(
                            Format('{item[title]}'),
                            id='visualisation_s',
                            items='visualisations',
                            item_id_getter=operator.itemgetter('id'),
                            on_click=select_visualisation
                        )
                    ),
    SwitchTo(Const('<< Назад'), id='back', state=StatisticState.choice_dashboard),
    parse_mode=ParseMode.HTML,
    getter=get_visualisations,
    state=StatisticState.choice_visualisation
)

visualisation_view = Window(
    Format('Визуализация'),
    DynamicMedia('file'),
    SwitchTo(Const('<< Назад'), id='back', state=StatisticState.choice_visualisation),
    getter=get_visualisation,
    state=StatisticState.visualisation_view
)

