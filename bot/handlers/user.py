from aiogram import types
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext

from bot.handlers.keyboards.inline.user import user_edit
from bot.handlers.keyboards.inline.user_callback_datas import edit_user_callback
from bot.states.user.edit_username import EditUsername
from database.user.sqlite import get_user_by_id, edit_user


async def command_user(message: types.Message):
    user = await get_user_by_id(user_id=message.from_user.id)

    await message.answer(text=f'user id: {user.get("user_id")}\n'
                              f'username: {user.get("username")}\n'
                              f'first name: {user.get("first_name")}\n'
                              f'last name: {user.get("last_name")}\n'
                              f'age: {user.get("age")}\n'
                              f'description: {user.get("description")}',
                         reply_markup=user_edit)

    await message.answer_photo(user.get('photo'))


async def edit_username_callback(call: types.CallbackQuery):
    await call.answer(text='enter new username')
    await EditUsername.InsertUsername.set()


async def edit_username(message: types.Message, state: FSMContext):
    await edit_user(user_id=message.from_user.id, username=message.text)
    await state.finish()


def register_user(dp: Dispatcher):
    dp.register_message_handler(command_user, state='*', commands=['user'])

    dp.register_callback_query_handler(edit_username_callback, edit_user_callback.filter(type='edit_username'))
    dp.register_message_handler(edit_username, state=EditUsername.InsertUsername)
