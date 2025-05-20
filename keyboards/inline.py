from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def questions_kb():
    builder=InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="1й вопрос", callback_data="question_1"),
        InlineKeyboardButton(text="2й вопрос", callback_data="question_2"),
        InlineKeyboardButton(text="3й вопрос", callback_data="question_3"),
        width=1
    )
    return builder.as_markup()

links_kb=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Белорусский сайт", url="https://colonwell.by/"),
        InlineKeyboardButton(text="Литовский сайт", url="https://colonwell.lt/"),
        InlineKeyboardButton(text="Казахский сайт", url="https://colonwell.kz/"),
        InlineKeyboardButton(text="Даня", url="tg://resolve?domain=danya_chaika")]
    ]
)