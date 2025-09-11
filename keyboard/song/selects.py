from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager

from .states import SongState

from keyboard.main.states import MainState
from keyboard.search.states import SearchState

from common_lib.api_client.client import url_f, api_client
from typing import Any

async def select_category(
        callback: CallbackQuery,
        widget: Any,
        dialog_manager: DialogManager,
        item_id: int
):
    ctx = dialog_manager.current_context()

    response = await api_client.call_async_get(
        params={
            'category_id': item_id
        },
        url=url_f.song_category_childrens
    )
    if not (categories := response['data']):
        ctx.dialog_data.update(
            category_id=item_id,
            current_category=item_id
        )

        await dialog_manager.switch_to(SongState.song_choice)

    else:
        ctx.dialog_data.update(
            current_category=item_id,
            children_categories=categories
        )

        await dialog_manager.switch_to(SongState.category_choice)

async def back_category(
        callback: CallbackQuery,
        widget: Any,
        dialog_manager: DialogManager,
):
    ctx = dialog_manager.current_context()

    if not (current_category := ctx.dialog_data.get('current_category')):
        await dialog_manager.start(MainState.main)
        return

    response = await api_client.call_async_get(
        params={
            'category_ids': [current_category]
        },
        url=url_f.base_url_song_category
    )

    current_category_data = response['data'][0]

    params = {
        'category_id': current_category_data['parent_id']
    } if current_category_data['parent_id'] else None

    response = await api_client.call_async_get(
        params=params,
        url=url_f.song_category_childrens
    )

    children_categories = response['data']

    ctx.dialog_data.update(
        children_categories=children_categories,
        current_category=current_category_data['parent_id']
    )

    ctx.dialog_data['category_title_stack'] = ctx.dialog_data.get('category_title_stack', [])[:-1]

    await dialog_manager.switch_to(SongState.category_choice)

async def select_song(
        callback: CallbackQuery,
        widget: Any,
        dialog_manager: DialogManager,
        item_id: int
):
    ctx = dialog_manager.current_context()
    ctx.dialog_data.update(song_id=item_id)

    await dialog_manager.switch_to(SongState.song_view)

async def back_song(
        callback: CallbackQuery,
        widget: Any,
        dialog_manager: DialogManager,
):
    ctx = dialog_manager.current_context()

    if start_data := ctx.start_data:
        await dialog_manager.start(SearchState.search_result, data={
            'search_items': start_data.get('search_items')
        })
    else:
        await dialog_manager.back()

