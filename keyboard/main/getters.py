from pathlib import Path

from aiogram_dialog import DialogManager
from common_lib.api_client.client import api_client, url_f

async def create_review(
        dialog_manager: DialogManager,
        **kwargs
):
    event = dialog_manager.event
    success = True
    try:
        response = await api_client.call_async_post(
            url=url_f.reviews,
            body={
                'id_user': event.from_user.id,
                'text_review': event.text,
                'created_data': str(event.date),
            }
        )
    except:
        success = False


    chat_id = dialog_manager.event.chat.id
    last_message_id = kwargs.get('aiogd_stack').last_message_id
    message_id = dialog_manager.event.message_id

    await kwargs.get('bot').delete_message(chat_id=chat_id, message_id=message_id)
    await kwargs.get('bot').delete_message(chat_id=chat_id, message_id=last_message_id)

    return {
        'success': success
    }

async def get_about_pipif(
        dialog_manager: DialogManager,
        **kwargs
):
    about_file = Path(Path(__file__).resolve().parents[2], 'common_lib/about_pipif.txt')
    with about_file.open('r') as f:
        about_text = f.read()

    return {
        'text': about_text,
    }