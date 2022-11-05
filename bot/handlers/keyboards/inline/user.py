from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.handlers.keyboards.inline.user_callback_datas import edit_user_callback

user_edit = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='edit username',
                callback_data=edit_user_callback.new(type='edit_username')
            ),
            InlineKeyboardButton(
                text='edit first name',
                callback_data=edit_user_callback.new(type='edit_first_name')
            )
        ],
        [
            InlineKeyboardButton(
                text='edit last name',
                callback_data=edit_user_callback.new(type='edit_last_name')
            ),
            InlineKeyboardButton(
                text='edit age',
                callback_data=edit_user_callback.new(type='edit_age')
            )
        ],
        [
            InlineKeyboardButton(
                text='edit description',
                callback_data=edit_user_callback.new(type='edit_description')
            ),
            InlineKeyboardButton(
                text='edit photo',
                callback_data=edit_user_callback.new(type='edit_photo')
            )
        ]
    ]
)