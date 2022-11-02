from aiogram.dispatcher.filters.state import StatesGroup, State


class QuadraticEquation(StatesGroup):
    NumberA = State()
    NumberB = State()
    NumberC = State()
    ReturnResult = State()
