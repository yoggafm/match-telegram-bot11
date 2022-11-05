from aiogram import types
from aiogram import Dispatcher

from bot.handlers.keyboards.inline.author import author


async def get_author_info(message: types.Message):
    await message.answer('Моя почта dan.bel.wsr@gmail.com', reply_markup=author)


def register_author(dp: Dispatcher):
    dp.register_message_handler(get_author_info, state='*', commands=['author'])
