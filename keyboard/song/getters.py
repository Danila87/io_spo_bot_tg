from aiogram_dialog import DialogManager

from common_lib.api_client.client import api_client, url_f
from typing import Dict

async def get_categories(
        dialog_manager: DialogManager,
        **kwargs
):
    ctx = dialog_manager.current_context()

    category_title_stack = ctx.dialog_data.get('category_title_stack', [])
    categories_data = []

    if current_category_id := ctx.dialog_data.get('current_category'):
        current_category_data = await api_client.call_async_get(
            url=url_f.song_category,
            params={'category_id': current_category_id}
        )

        if not category_title_stack or category_title_stack[-1] != current_category_data['name']:
            category_title_stack.append(current_category_data['name'])

        ctx.dialog_data.update(category_title_stack=category_title_stack)

    if children_categories := ctx.dialog_data.get('children_categories'):
        categories_data = children_categories

    elif categories := await api_client.call_async_get(
        url=url_f.main_song_categories
    ):
        categories_data = categories

    return {
        'current_song_category_title': ' / '.join(category_title_stack) if category_title_stack else 'Выбор категории',
        'count': len(categories_data),
        'data': categories_data
    }

async def get_songs(
        dialog_manager: DialogManager,
        **kwargs
) -> Dict:
    ctx = dialog_manager.current_context()
    category_id = ctx.dialog_data.get('current_category')
    songs = await api_client.call_async_get(
        url=url_f.sons_by_category,
        params={
            'category_id': int(category_id)
        })

    return {
        'data': songs,
        'available': True if songs else False
    }

async def get_song(
        dialog_manager: DialogManager,
        **kwargs
) -> Dict:
    ctx = dialog_manager.current_context()
    song_id = ctx.start_data.get('search_id') if ctx.start_data else None

    return {
        'song': await api_client.call_async_get(
        url=url_f.base_url_song,
        params={
            'song_id': song_id if song_id else ctx.dialog_data.get('song_id')
        }
    )
    }