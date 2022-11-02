from aiogram import Dispatcher
from aiogram.types import Message


async def start_bot(message: Message):
    await message.answer('Start, Bot!')


def register_start_bot(dp: Dispatcher):
    dp.register_message_handler(start_bot, commands=['start'], state='*')
