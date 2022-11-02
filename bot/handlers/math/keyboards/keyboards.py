from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_next_exit = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Next'),
            KeyboardButton(text='Exit')
        ]
    ],
    resize_keyboard=True
)

menu_simple_math_actions = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='+'),
            KeyboardButton(text='-'),
        ],
        [
            KeyboardButton(text='×'),
            KeyboardButton(text='÷'),
        ]
    ],
    resize_keyboard=True
)
