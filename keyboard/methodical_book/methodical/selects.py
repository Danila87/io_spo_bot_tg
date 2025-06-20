from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager

from keyboard.methodical_book.states import MethodicalBook

from common_lib.api_client.client import url_f, api_client
from typing import Any

from keyboard.methodical_book.methodical.states import Methodical


async def select_chapter(
        callback: CallbackQuery,
        widget: Any,
        dialog_manager: DialogManager,
        item_id: int
):
    ctx = dialog_manager.current_context()

    if not (children_chapters := await api_client.call_async_get(
        params={
            'id_chapter': item_id
        },
        url=url_f.chapters_children
    )):
        ctx.dialog_data.update(
            chapter_id=item_id,
            current_chapter=item_id,
            children_chapters=[]
        )

    else:
        ctx.dialog_data.update(
            current_chapter=item_id,
            children_chapters=children_chapters
        )

    await dialog_manager.switch_to(Methodical.main_view)

async def back_chapter(
        callback: CallbackQuery,
        widget: Any,
        dialog_manager: DialogManager,
):
    ctx = dialog_manager.current_context()

    if not (current_chapter := ctx.dialog_data.get('current_chapter')):
        await dialog_manager.start(MethodicalBook.main)
        return

    current_chapter_data = await api_client.call_async_get(
        params={
            'id_chapter': current_chapter
        },
        url=url_f.chapters
    )

    params = {
        'id_chapter': current_chapter_data['parent_id']
    } if current_chapter_data['parent_id'] else None

    children_chapters = await api_client.call_async_get(
        params=params,
        url=url_f.chapters_children
    )

    ctx.dialog_data.update(
        children_chapters=children_chapters,
        current_chapter=current_chapter_data['parent_id']
    )

    ctx.dialog_data['chapter_title_stack'] = ctx.dialog_data.get('chapter_title_stack', [])[:-1]

    await dialog_manager.switch_to(Methodical.main_view)