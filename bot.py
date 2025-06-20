from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from aiogram_dialog import setup_dialogs

from config import BOT_TOKEN

from keyboard.main.dialogs import main_dialog
from keyboard.song.dialogs import song_dialog

from keyboard.methodical_book.dialogs import methodical_book_dialog

from keyboard.methodical_book.piggy_bank.dialogs import piggy_bank_dialog
from keyboard.methodical_book.piggy_bank.games.dialogs import games_dialog
from keyboard.methodical_book.piggy_bank.legends.dialogs import legend_dialog
from keyboard.methodical_book.piggy_bank.ktd.dialogs import ktd_dialog
from keyboard.statistic.dialogs import statistic_dialog
from keyboard.methodical_book.methodical.dialogs import methodical_dialog

from keyboard.search.dialogs import search_dialog

from middleware import middleware

bot = Bot(token=BOT_TOKEN)

storage = MemoryStorage()

dp = Dispatcher(bot=bot, storage=storage)

# Требует реализации
# dp.message.outer_middleware(Mute())

# Временно отключено
dp.update.outer_middleware(middleware.CheckUserRegistration())

dp.include_router(main_dialog)
dp.include_router(song_dialog)
dp.include_router(methodical_book_dialog)
dp.include_router(piggy_bank_dialog)
dp.include_router(games_dialog)
dp.include_router(legend_dialog)
dp.include_router(ktd_dialog)
dp.include_router(methodical_dialog)
dp.include_router(search_dialog)
dp.include_router(statistic_dialog)


# Регистрируем диалоги
setup_dialogs(dp)
