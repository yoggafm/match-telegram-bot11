from aiogram.dispatcher.filters.state import StatesGroup, State


class EditUsername(StatesGroup):
    InsertUsername = State()
