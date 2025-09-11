from aiogram_dialog import DialogManager

from common_lib.api_client.client import api_client, url_f
from common_lib.utils import get_file
from typing import Dict

async def get_chapters(
        dialog_manager: DialogManager,
        **kwargs
) -> Dict:
    ctx = dialog_manager.current_context()

    chapter_title_stack = ctx.dialog_data.get('chapter_title_stack', [])

    chapters_data = []
    file = None

    if current_chapter_id := ctx.dialog_data.get('current_chapter'):
        response = await api_client.call_async_get(
            url=url_f.base_url_methodical_book,
            params={'chapter_ids': [current_chapter_id]}
        )
        if not chapter_title_stack or chapter_title_stack[-1] != response['data'][0]['title']:
            chapter_title_stack.append(response['data'][0]['title'])
            ctx.dialog_data.update(chapter_title_stack=chapter_title_stack)

        file = await get_file(
            url=url_f.methodical_book_file,
            params={
                'chapter_id': current_chapter_id
            }
        )

    if children_chapter := ctx.dialog_data.get('children_chapters'):
            chapters_data = children_chapter

    response =  await api_client.call_async_get(
        url=url_f.base_url_methodical_book,
        params={"is_only_parents": "true"}
    )
    if (chapters := response['data']) and not current_chapter_id:
            chapters_data = chapters

    return {
        'current_chapter_title': ' / '.join(chapter_title_stack) if chapter_title_stack else 'Выбор главы',
        'data': chapters_data,
        'file': file,
        'available': True if file or chapters_data else False
    }
