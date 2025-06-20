from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Callable, Dict, Awaitable, Any

from common_lib.api_client.client import api_client, url_f

NOT_REMOTE_COMMANDS: list[str] = ['/start', '/getMenuTest']


class CheckUserRegistration(BaseMiddleware):

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:

        payload = {
                  "telegram_id": data['event_from_user'].id,
                  "first_name": data['event_from_user'].first_name,
                  "last_name": data['event_from_user'].last_name,
                  "nickname": data['event_from_user'].username
                }
        await api_client.call_async_post(
            url=url_f.check_user,
            body=payload
        )

        return await handler(event, data)


class Mute(BaseMiddleware):

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any],
            mute: int = 5
    ) -> Any:

        return await handler(event, data)
