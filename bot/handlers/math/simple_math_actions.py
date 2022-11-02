from aiogram import types
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext

from bot.states.math.simple_math_actions import SimpleMathActions
from bot.handlers.math.keyboards import keyboards

simple_math_actions_info = 'Простые математические действия: \nсложение, вычитание, умножение, деление.'
exit_text = 'Exit simple math actions'


async def enter_simple_math_actions(message: types.Message):
    await message.answer(
        text=simple_math_actions_info,
        reply_markup=keyboards.menu_next_exit
    )

    await SimpleMathActions.NumberOne.set()


async def answer_number_one(message: types.Message, state: FSMContext):
    answer = message.text

    if answer == 'Next':
        await message.answer('enter number one', reply_markup=types.ReplyKeyboardRemove())
        await SimpleMathActions.next()
    elif answer == 'Exit':
        await message.answer(exit_text, reply_markup=types.ReplyKeyboardRemove())
        await state.finish()
    else:
        await message.answer(
            text=simple_math_actions_info,
            reply_markup=keyboards.menu_next_exit
        )


async def answer_number_two(message: types.Message, state: FSMContext):
    number_one = message.text

    if number_one \
            .replace(".", "", 1).replace('-', '', 1).isdigit():
        await message.answer('enter number two')
        await state.update_data(number_one=number_one)
        await SimpleMathActions.next()
    else:
        await message.answer('enter number one')


async def answer_action(message: types.Message, state: FSMContext):
    number_two = message.text

    if number_two \
            .replace(".", "", 1).replace('-', '', 1).isdigit():
        await message.answer('enter action', reply_markup=keyboards.menu_simple_math_actions)
        await state.update_data(number_two=number_two)
        await SimpleMathActions.next()
    else:
        await message.answer('enter number two')


async def answer_finish(message: types.Message, state: FSMContext):
    data = await state.get_data()

    number_one = float(data.get('number_one'))
    number_two = float(data.get('number_two'))
    action = message.text

    if action == '+' or action == '-' or action == '×' or action == '÷':
        result = solution(number_one=number_one, number_two=number_two, action=action)
        await message.answer(text=str(round(result, 3)), reply_markup=types.ReplyKeyboardRemove())
        await state.finish()
    else:
        await message.answer('enter action', reply_markup=keyboards.menu_simple_math_actions)


def solution(number_one: float, number_two: float, action: str):
    if action == '+':
        return number_one + number_two
    elif action == '-':
        return number_one - number_two
    elif action == '×':
        return number_one * number_two
    elif action == '÷':
        return number_one / number_two
    else:
        raise Exception('action: + or - or × or ÷')


def register_simple_math_actions(dp: Dispatcher):
    dp.register_message_handler(enter_simple_math_actions, commands=["simple_math_actions"], state='*')
    dp.register_message_handler(answer_number_one, state=SimpleMathActions.NumberOne)
    dp.register_message_handler(answer_number_two, state=SimpleMathActions.NumberTwo)
    dp.register_message_handler(answer_action, state=SimpleMathActions.Action)
    dp.register_message_handler(answer_finish, state=SimpleMathActions.Finish)
