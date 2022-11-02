from aiogram.dispatcher.filters.state import StatesGroup, State


class SimpleMathActions(StatesGroup):
    NumberOne = State()
    NumberTwo = State()
    Action = State()
    Finish = State()
