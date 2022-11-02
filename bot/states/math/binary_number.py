from aiogram.dispatcher.filters.state import StatesGroup, State


class BinaryNumber(StatesGroup):
    InputNumber = State()
    ReturnResult = State()
