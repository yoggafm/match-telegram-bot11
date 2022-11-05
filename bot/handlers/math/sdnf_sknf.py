from aiogram import types
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext

from bot.math.sdnf_sknf import sdnf_sknf
from bot.states.math.sdnf_sknf import SdnfSknf


async def enter_sdnf_sknf(message: types.Message):
    await message.answer('Видите x1 в формате 0;1;0;1 и т.д')
    await SdnfSknf.InsertX1.set()


async def answer_x1(message: types.Message, state: FSMContext):
    x1 = message.text.split(';')
    await message.answer('Видите x2 в формате 0;1;0;1 и т.д')
    await state.update_data(x1=x1)
    await SdnfSknf.next()


async def answer_x2(message: types.Message, state: FSMContext):
    x2 = message.text.split(';')
    await message.answer('Видите x3 в формате 0;1;0;1 и т.д')
    await state.update_data(x2=x2)
    await SdnfSknf.next()


async def answer_x3(message: types.Message, state: FSMContext):
    x3 = message.text.split(';')
    await message.answer('Видите f в формате 0;1;0;1 и т.д')
    await state.update_data(x3=x3)
    await SdnfSknf.next()


async def answer_f(message: types.Message, state: FSMContext):
    data = await state.get_data()
    x1 = data.get('x1')
    x2 = data.get('x2')
    x3 = data.get('x3')
    f = message.text.split(';')

    sdnfSknf = sdnf_sknf(x1s=x1, x2s=x2, x3s=x3, f=f)

    await message.answer(text=f"sdnf: {sdnfSknf['sdnf']}")
    await message.answer(text=f"sknf: {sdnfSknf['sknf']}")
    await message.answer(text=f"conjugation elements:\n{sdnfSknf['conjugationElements']}")
    await message.answer(text=f"disjunction elements:\n{sdnfSknf['disjunctionElements']}")
    await state.finish()


def register_sdnf_sknf(dp: Dispatcher):
    dp.register_message_handler(enter_sdnf_sknf, commands='sdnf_sknf', state='*')
    dp.register_message_handler(answer_x1, state=SdnfSknf.InsertX1)
    dp.register_message_handler(answer_x2, state=SdnfSknf.InsertX2)
    dp.register_message_handler(answer_x3, state=SdnfSknf.InsertX3)
    dp.register_message_handler(answer_f, state=SdnfSknf.InsertF)
