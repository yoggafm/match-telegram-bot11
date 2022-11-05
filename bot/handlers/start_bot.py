from aiogram import Dispatcher
from aiogram.types import Message

from database.user.sqlite import create_user


async def start_bot(message: Message):
    await message.answer_sticker('CAACAgIAAxkBAAEGSfhjYoFIG5zGxFrkQc_oZmJ0T4snHwACcRUAAhQkyUg9cG3f7HC5TioE')
    await message.answer('Start, Bot!')

    photos = await message.from_user.get_profile_photos()
    photo_id = photos['photos'][0][0]['file_id']

    await create_user(user_id=message.from_user.id, username=message.from_user.username,
                      last_name=message.from_user.last_name, first_name=message.from_user.first_name,
                      photo=photo_id)


def register_start_bot(dp: Dispatcher):
    dp.register_message_handler(start_bot, commands=['start'], state='*')
