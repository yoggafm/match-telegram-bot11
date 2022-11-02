from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.handlers.math.keyboards.inline.callback_datas import next_callback, exit_callback, binary_number_callback, \
    back_callback

binary_number = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Next',
                callback_data=next_callback.new()
            ),
            InlineKeyboardButton(
                text='Exit',
                callback_data=exit_callback.new()
            ),
        ]
    ]
)

binary_number_types = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='from 10 to 2',
                callback_data=binary_number_callback.new(from_='10', to_='2')
            ),
            InlineKeyboardButton(
                text='from 2 to 10',
                callback_data=binary_number_callback.new(from_='2', to_='10')
            )
        ],
        [
            InlineKeyboardButton(
                text='Back',
                callback_data=back_callback.new()
            )
        ]
    ]
)
