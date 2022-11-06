from aiogram.dispatcher.filters.state import StatesGroup, State


class EditFirstName(StatesGroup):
    InsertFirstName = State()
