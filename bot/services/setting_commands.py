from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_default_commands(bot: Bot):
    return await bot.set_my_commands(
        commands=[
            BotCommand('simple_math_actions', 'Простые математические действия'),
            BotCommand('quadratic_equation', 'Квадратное уравнение'),
            BotCommand('binary_number', 'Двоичная система счисления'),
            BotCommand('truth_table', 'Таблица истинности'),
            BotCommand('sdnf_sknf', 'СДНФ и СКНФ'),
            BotCommand('user', 'информация об пользователи'),
            BotCommand('author', 'информация об авторе')
        ],
        scope=BotCommandScopeDefault()
    )
