from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
back_btn = KeyboardButton(text="назад")
main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="каталог"), KeyboardButton(text="контакты")],
        [KeyboardButton(text="информация"), KeyboardButton(text="истории успеха")],
        [KeyboardButton(text="вопросы"), KeyboardButton(text="корзина")]
    ],
    resize_keyboard=True,
    input_field_placeholder="что хотите?"
)
catalog_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="1-й продукт"), KeyboardButton(text="2-й продукт")],
        [KeyboardButton(text="3-й продукт"), KeyboardButton(text="4-й продукт")],
        [KeyboardButton(text="5-й продукт"), KeyboardButton(text="6-й продукт")],
        [back_btn]
    ],
    resize_keyboard=True,
    input_field_placeholder="что хотите?"
)
stories_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="1-я история"), KeyboardButton(text="2-я история")],
        [KeyboardButton(text="3-я история"), KeyboardButton(text="4-я история")],
        [KeyboardButton(text="5-я история"), KeyboardButton(text="6-я история")]
    ],
    resize_keyboard=True,
    input_field_placeholder="что хотите?"
)
questions_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="1-й вопрос"), KeyboardButton(text="2-й вопрос")],
        [KeyboardButton(text="3-й вопрос"), KeyboardButton(text="4-й вопрос")],
    ],
    resize_keyboard=True,
    input_field_placeholder="что хотите?"
)
cart_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="удалить из корзины"), KeyboardButton(text="оплатить")],
        [KeyboardButton(text="общая стоимость")]
    ],
    resize_keyboard=True,
    input_field_placeholder="что хотите?"
)
about_us_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="информация о нас")]
    ],
    resize_keyboard=True,
    input_field_placeholder="что хотите?"
)