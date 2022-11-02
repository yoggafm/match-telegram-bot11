from aiogram import types
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext

from bot.math.quadratic_equation import quadratic_equation
from bot.states.math.quadratic_equation import QuadraticEquation
from bot.handlers.math.keyboards import keyboards

quadratic_equation_info = 'Уравнение вида a x 2 + bx + c = 0 , в котором a, b и c — действительные числа, и a ≠ 0 , ' \
                          'называется квадратным уравнением. '
exit_text = 'Exit quadratic equation'


async def enter_quadratic_equation(message: types.Message):
    await message.answer(
        text=quadratic_equation_info,
        reply_markup=keyboards.menu_next_exit
    )

    await QuadraticEquation.NumberA.set()


async def answer_number_a(message: types.Message, state: FSMContext):
    answer = message.text

    if answer == 'Next':
        await message.answer('enter number a', reply_markup=types.ReplyKeyboardRemove())
        await QuadraticEquation.next()
    elif answer == 'Exit':
        await message.answer(exit_text, reply_markup=types.ReplyKeyboardRemove())
        await state.finish()
    else:
        await message.answer(
            text=quadratic_equation_info,
            reply_markup=keyboards.menu_next_exit
        )


async def answer_number_b(message: types.Message, state: FSMContext):
    number_a = message.text

    if number_a \
            .replace(".", "", 1).replace('-', '', 1).isdigit():
        await message.answer('enter number b')
        await state.update_data(number_a=number_a)
        await QuadraticEquation.next()
    else:
        await message.answer('enter number a')


async def answer_number_c(message: types.Message, state: FSMContext):
    number_b = message.text

    if number_b \
            .replace(".", "", 1).replace('-', '', 1).isdigit():
        await message.answer('enter number c')
        await state.update_data(number_b=number_b)
        await QuadraticEquation.next()
    else:
        await message.answer('enter number b')


async def answer_return_result(message: types.Message, state: FSMContext):
    data = await state.get_data()

    number_a = float(data.get('number_a'))
    number_b = float(data.get('number_b'))
    number_c = message.text

    if number_c \
            .replace(".", "", 1).replace('-', '', 1).isdigit():
        result = quadratic_equation(a=number_a, b=number_b, c=float(number_c))
        await message.answer(result['message'])
        await message.answer('x1: ' + str(result['x1']))
        await message.answer('x2: ' + str(result['x2']))
        await message.answer('discriminant: ' + str(result['discriminant']))
        await state.finish()
    else:
        await message.answer('enter number c')


def register_quadratic_equation(dp: Dispatcher):
    dp.register_message_handler(enter_quadratic_equation, commands=["quadratic_equation"], state='*')
    dp.register_message_handler(answer_number_a, state=QuadraticEquation.NumberA)
    dp.register_message_handler(answer_number_b, state=QuadraticEquation.NumberB)
    dp.register_message_handler(answer_number_c, state=QuadraticEquation.NumberC)
    dp.register_message_handler(answer_return_result, state=QuadraticEquation.ReturnResult)
