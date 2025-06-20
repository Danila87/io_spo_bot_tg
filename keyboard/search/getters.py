from aiogram_dialog import DialogManager

from common_lib.api_client.client import api_client, url_f

async def get_search_data(
        dialog_manager: DialogManager,
        **kwargs
):
    ctx = dialog_manager.current_context()

    if start_data := ctx.start_data:
        if 'search_items' in start_data:
            data = start_data.get('search_items')
            ctx.dialog_data.update(search_items=data)
            return data

    title = ctx.widget_data['search_title']

    data = await api_client.call_async_get(
        url=url_f.search_by_title,
        params={
            'title': title
        }
    )

    data['available'] = True if any(value for value in data.values()) else False

    ctx.dialog_data.update(search_items=data)

    if hasattr(dialog_manager.event, 'chat'):
        chat_id = dialog_manager.event.chat.id
        last_message_id = kwargs.get('aiogd_stack').last_message_id
        message_id = dialog_manager.event.message_id

        await kwargs.get('bot').delete_message(chat_id=chat_id, message_id=message_id)
        await kwargs.get('bot').delete_message(chat_id=chat_id, message_id=last_message_id)

    return data