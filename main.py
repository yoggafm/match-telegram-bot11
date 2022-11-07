import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.executor import start_webhook

from bot.handlers.author import register_author
from bot.handlers.errors.errors_handler import register_errors_handler
from bot.handlers.math.binary_number import register_binary_number
from bot.handlers.math.quadratic_equation import register_quadratic_equation
from bot.data.config import BOT_TOKEN, WEBHOOK_URL, WEBHOOK_PATH, WEBAPP_HOST, WEBAPP_PORT
from bot.handlers.math.sdnf_sknf import register_sdnf_sknf

from bot.handlers.start_bot import register_start_bot
from bot.handlers.math.simple_math_actions import register_simple_math_actions
from bot.handlers.user import register_user
from bot.services.setting_commands import set_default_commands
from database.user.sqlite import db_start

bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())


def register_all_handlers():
    register_start_bot(dp)

    register_simple_math_actions(dp)
    register_quadratic_equation(dp)
    register_binary_number(dp)
    register_sdnf_sknf(dp)

    register_author(dp)
    register_user(dp)

    register_errors_handler(dp)


async def set_all_default_commands():
    await set_default_commands(bot)


async def on_startup(_):
    await db_start()
    # await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)


async def on_shutdown(_):
    await bot.delete_webhook()


async def main():
    await set_all_default_commands()

    register_all_handlers()

    try:
        logging.basicConfig(level=logging.INFO)
        # await start_webhook(
        #     dispatcher=dp,
        #     webhook_path=WEBHOOK_PATH,
        #     skip_updates=True,
        #     host=WEBAPP_HOST,
        #     port=WEBAPP_PORT,
        #     on_startup=on_startup,
        #     on_shutdown=on_shutdown
        # )
        await on_startup(dp)
        await dp.start_polling()
    finally:
        await bot.delete_webhook()
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
