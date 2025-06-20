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
        current_chapter = await api_client.call_async_get(
            url=url_f.chapters,
            params={'id_chapter': current_chapter_id}
        )
        if not chapter_title_stack or chapter_title_stack[-1] != current_chapter['title']:
            chapter_title_stack.append(current_chapter['title'])
            ctx.dialog_data.update(chapter_title_stack=chapter_title_stack)

        file = await get_file(
            url=url_f.chapters_file,
            params={
                'chapter_id': current_chapter_id
            }
        )

    if children_chapter := ctx.dialog_data.get('children_chapters'):
            chapters_data = children_chapter

    if (chapters := await api_client.call_async_get(
        url=url_f.chapters_main
    )) and not current_chapter_id:
            chapters_data = chapters

    return {
        'current_chapter_title': ' / '.join(chapter_title_stack) if chapter_title_stack else 'Выбор главы',
        'data': chapters_data,
        'file': file,
        'available': True if file or chapters_data else False
    }
