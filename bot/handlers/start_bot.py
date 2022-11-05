from aiogram import Dispatcher
from aiogram.types import Message


async def start_bot(message: Message):
    await message.answer_sticker('CAACAgIAAxkBAAEGSfhjYoFIG5zGxFrkQc_oZmJ0T4snHwACcRUAAhQkyUg9cG3f7HC5TioE')
    await message.answer('Start, Bot!')


def register_start_bot(dp: Dispatcher):
    dp.register_message_handler(start_bot, commands=['start'], state='*')
