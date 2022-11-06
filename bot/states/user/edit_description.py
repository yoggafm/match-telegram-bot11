from aiogram.dispatcher.filters.state import StatesGroup, State


class EditDescription(StatesGroup):
    InsertDescription = State()
