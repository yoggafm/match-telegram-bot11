from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

author = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='GitHub',
                url='https://github.com/Danila009'
            )
        ]
    ]
)
