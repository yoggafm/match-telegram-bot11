from aiogram import types
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext

from bot.handlers.math.keyboards.inline.binary_number_buttons import binary_number, binary_number_types
from bot.handlers.math.keyboards.inline.callback_datas import next_callback, exit_callback, binary_number_callback, \
    back_callback
from bot.states.math.binary_number import BinaryNumber


async def enter_binary_number(message: types.Message):
    await message.answer("Перевод из десятичной в двоичную и обратно", reply_markup=binary_number)
    await BinaryNumber.InputNumber.set()


async def next_binary_number(call: types.CallbackQuery):
    await call.answer('exit_binary_number', cache_time=1)

    await call.message.edit_reply_markup(reply_markup=binary_number_types)


async def exit_binary_number(call: types.CallbackQuery, state: FSMContext):
    await call.answer('exit_binary_number', cache_time=1)

    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer(text='exit binary number')
    await state.finish()


async def back_reply_markup(call: types.CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=binary_number)


async def binary_number_type(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    from_ = callback_data.get('from_')
    to_ = callback_data.get('to_')

    await BinaryNumber.next()
    await state.update_data(from_=from_, to_=to_)
    await call.message.answer(text=f'input number')


async def answer_result(message: types.Message, state: FSMContext):
    data = await state.get_data()
    number = message.text
    from_ = data.get('from_')
    to_ = data.get('to_')

    if from_ == '2' and to_ == '10':
        await message.answer(f'Result: {str(int(number, 2))}')
    elif from_ == '10' and to_ == '2':
        await message.answer(f'Result: {str(bin(int(number)))}')

    await state.finish()


def register_binary_number(dp: Dispatcher):
    dp.register_message_handler(enter_binary_number, commands=['binary_number'], state="*")

    dp.register_callback_query_handler(
        next_binary_number,
        next_callback.filter(),
        state=BinaryNumber.InputNumber
    )
    dp.register_callback_query_handler(
        exit_binary_number,
        exit_callback.filter(),
        state=BinaryNumber.InputNumber
    )

    dp.register_callback_query_handler(
        back_reply_markup,
        back_callback.filter(),
        state=BinaryNumber.InputNumber
    )

    dp.register_callback_query_handler(
        binary_number_type,
        binary_number_callback.filter(),
        state=BinaryNumber.InputNumber
    )

    dp.register_message_handler(
        answer_result,
        state=BinaryNumber.ReturnResult
    )
