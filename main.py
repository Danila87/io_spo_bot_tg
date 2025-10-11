import asyncio
import logging

from aiogram.filters import Command, CommandStart
from aiogram import types, F

from aiogram_dialog import DialogManager, StartMode

from bot import bot, dp

from keyboard.main.states import MainState
from prometheus_client import start_http_server

@dp.message(CommandStart())
async def start(
        message: types.Message,
):
    await message.answer(
        'Добро пожаловать в бота!\n'
        'Для вызова меню введи команду /get_menu.\n'
        'Для поиска песни просто введи ее название.'
    )


@dp.message(Command('get_menu'))
async def get_menu(
        message: types.Message,
        dialog_manager: DialogManager
):
    await dialog_manager.start(
        MainState.main,
        mode=StartMode.RESET_STACK
    )


async def main():

    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    start_http_server(8000)
    asyncio.run(main())