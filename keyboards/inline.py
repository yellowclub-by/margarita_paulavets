from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

def questions_kb():
    builder=InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="1й вопрос", callback_data="question_1"),
        InlineKeyboardButton(text="2й вопрос", callback_data="question_2"),
        InlineKeyboardButton(text="3й вопрос", callback_data="question_3"),
        width=1
    )
    return builder.as_markup()