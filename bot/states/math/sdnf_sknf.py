from aiogram.dispatcher.filters.state import StatesGroup, State


class SdnfSknf(StatesGroup):
    InsertX1 = State()
    InsertX2 = State()
    InsertX3 = State()
    InsertF = State()