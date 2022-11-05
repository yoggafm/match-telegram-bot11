import asyncio

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from bot.handlers.errors.errors_handler import register_errors_handler
from bot.handlers.math.binary_number import register_binary_number
from bot.handlers.math.quadratic_equation import register_quadratic_equation
from bot.data.config import BOT_TOKEN
from bot.handlers.math.sdnf_sknf import register_sdnf_sknf

from bot.handlers.start_bot import register_start_bot
from bot.handlers.math.simple_math_actions import register_simple_math_actions
from bot.services.setting_commands import set_default_commands


def register_all_handlers(dp):
    register_start_bot(dp)

    register_simple_math_actions(dp)
    register_quadratic_equation(dp)
    register_binary_number(dp)
    register_sdnf_sknf(dp)

    register_errors_handler(dp)


async def set_all_default_commands(bot: Bot):
    await set_default_commands(bot)


async def main():
    bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
    dp = Dispatcher(bot, storage=MemoryStorage())

    await set_all_default_commands(bot)

    register_all_handlers(dp)

    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
