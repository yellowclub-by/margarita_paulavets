from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command


user_router=Router()


@user_router.message(CommandStart())
async def start(message: types.Message):
    await (message.answer("привет"))

@user_router.message(F.text.lower().contains("каталог"))
@user_router.message(Command("catalog"))
async def catalog(message: types.Message):
    await (message.answer("вы открыли каталог"))

@user_router.message(F.text.lower().contains("контакт"))
@user_router.message(Command("contacts"))
async def contacts(message: types.Message):
    await (message.answer("вот наши контакты"))

@user_router.message(F.text.lower().contains("инф"))
@user_router.message(Command("about_us"))
async def about_us(message: types.Message):
    await (message.answer("вот информация о нас"))



@user_router.message(F.text.lower().contains("истор")|F.text.lower().endswith("успех"))
async def stories(message: types.Message):
    await (message.answer("вот наши истории успеха"))

@user_router.message(F.text.lower().contains("часто")|F.text.lower().endswith("вопрос"))
async def questions(message: types.Message):
    await (message.answer("вот часто задаваемые вопросы"))

@user_router.message(F.text.lower().contains("корзин"))
@user_router.message(Command("cart"))
async def cart(message: types.Message):
    await (message.answer("вот корзина"))

# @user_router.message(F.text.lower().contains("цен")|F.text.lower().endswith("?"))
# async def echo(message: types.Message):
#     await (message.answer("бот в разработке"))
    # user_text=message.text
    # await (message.answer(user_text))