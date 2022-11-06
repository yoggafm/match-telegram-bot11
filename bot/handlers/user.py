from aiogram import types
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext

from bot.handlers.keyboards.inline.user import user_edit
from bot.handlers.keyboards.inline.user_callback_datas import edit_user_callback
from bot.states.user.edit_age import EditAge
from bot.states.user.edit_description import EditDescription
from bot.states.user.edit_first_name import EditFirstName
from bot.states.user.edit_last_name import EditLastName
from bot.states.user.edit_photo import EditPhoto
from bot.states.user.edit_username import EditUsername
import database.user.sqlite as user_db


async def command_user(message: types.Message):
    user = await user_db.get_user_by_id(user_id=message.from_user.id)

    await message.answer(text=f'user id: {user.get("user_id")}\n'
                              f'username: {user.get("username")}\n'
                              f'first name: {user.get("first_name")}\n'
                              f'last name: {user.get("last_name")}\n'
                              f'age: {user.get("age")}\n'
                              f'description: {user.get("description")}', reply_markup=user_edit)

    await message.answer_photo(user.get('photo'))


async def edit_username_callback(call: types.CallbackQuery):
    await call.message.answer(text='enter new username')
    await EditUsername.InsertUsername.set()


async def edit_username(message: types.Message, state: FSMContext):
    try:
        await user_db.edit_username(user_id=message.from_user.id, username=message.text)
        await message.answer('successfully')
    except Exception as er:
        await message.answer(text=f"Error: {er}")
    finally:
        await state.finish()


async def edit_first_name_callback(call: types.CallbackQuery):
    await call.message.answer(text='enter new first name')
    await EditFirstName.InsertFirstName.set()


async def edit_first_name(message: types.Message, state: FSMContext):
    try:
        await user_db.edit_first_name(user_id=message.from_user.id, first_name=message.text)
        await message.answer('successfully')
    except Exception as er:
        await message.answer(text=f"Error: {er}")
    finally:
        await state.finish()


async def edit_last_name_callback(call: types.CallbackQuery):
    await call.message.answer(text='enter new last name')
    await EditLastName.InsertLastName.set()


async def edit_last_name(message: types.Message, state: FSMContext):
    try:
        await user_db.edit_last_name(user_id=message.from_user.id, last_name=message.text)
        await message.answer('successfully')
    except Exception as er:
        await message.answer(text=f"Error: {er}")
    finally:
        await state.finish()


async def edit_age_callback(call: types.CallbackQuery):
    await call.message.answer(text='enter new age')
    await EditAge.InsertAge.set()


async def edit_age(message: types.Message, state: FSMContext):
    try:
        await user_db.edit_age(user_id=message.from_user.id, age=int(message.text))
        await message.answer('successfully')
    except Exception as er:
        await message.answer(text=f"Error: {er}")
    finally:
        await state.finish()


async def edit_description_callback(call: types.CallbackQuery):
    await call.message.answer(text='enter new description')
    await EditDescription.InsertDescription.set()


async def edit_description(message: types.Message, state: FSMContext):
    try:
        await user_db.edit_description(user_id=message.from_user.id, description=message.text)
        await message.answer('successfully')
    except Exception as er:
        await message.answer(text=f"Error: {er}")
    finally:
        await state.finish()


async def edit_photo_callback(call: types.CallbackQuery):
    await call.message.answer(text='enter new photo')
    await EditPhoto.InsertPhoto.set()


async def edit_photo(message: types.Message, state: FSMContext):
    try:
        await user_db.edit_photo(user_id=message.from_user.id, photo=message.photo[-1].file_id)
        await message.answer('successfully')
    except Exception as er:
        await message.answer(text=f"Error: {er}")
    finally:
        await state.finish()


def register_user(dp: Dispatcher):
    dp.register_message_handler(command_user, state='*', commands=['user'])

    dp.register_callback_query_handler(edit_username_callback, edit_user_callback.filter(type='edit_username'))
    dp.register_message_handler(edit_username, state=EditUsername.InsertUsername)

    dp.register_callback_query_handler(edit_first_name_callback, edit_user_callback.filter(type='edit_first_name'))
    dp.register_message_handler(edit_first_name, state=EditFirstName.InsertFirstName)

    dp.register_callback_query_handler(edit_last_name_callback, edit_user_callback.filter(type='edit_last_name'))
    dp.register_message_handler(edit_last_name, state=EditLastName.InsertLastName)

    dp.register_callback_query_handler(edit_age_callback, edit_user_callback.filter(type='edit_age'))
    dp.register_message_handler(edit_age, state=EditAge.InsertAge)

    dp.register_callback_query_handler(edit_description_callback, edit_user_callback.filter(type='edit_description'))
    dp.register_message_handler(edit_description, state=EditDescription.InsertDescription)

    dp.register_callback_query_handler(edit_photo_callback, edit_user_callback.filter(type='edit_photo'))
    dp.register_message_handler(edit_photo, state=EditPhoto.InsertPhoto,content_types=['photo'])
