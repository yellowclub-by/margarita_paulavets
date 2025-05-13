from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
from keyboards import reply, inline


user_router=Router()


@user_router.message(CommandStart())
async def start(message: types.Message):
    await (message.answer("привет", reply_markup=reply.main_kb))

@user_router.message(F.text.lower()==("каталог"))
@user_router.message(Command("catalog"))
async def catalog(message: types.Message):
    await (message.answer("вы открыли каталог", reply_markup=reply.catalog_kb))

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

@user_router.message(F.text.lower().contains("вопрос"))
async def questions(message: types.Message):
    await message.answer("вот часто задаваемые вопросы", reply_markup=inline.questions_kb())

@user_router.callback_query(F.data.startswith("question"))
async def answers(callback: types.callback_query):
    query=callback.data.split("_")[1]
    if query=="1":
        await callback.message.answer("1")
    elif query=="2":
        await callback.message.answer("2")
    elif query=="3":
        await callback.message.answer("3")

    await callback.answer("ответ отправлен")

@user_router.message(F.text.lower().contains("корзин"))
@user_router.message(Command("cart"))
async def cart(message: types.Message):
    await (message.answer("вот корзина"))

# @user_router.message(F.text.lower().contains("цен")|F.text.lower().endswith("?"))
# async def echo(message: types.Message):
#     await (message.answer("бот в разработке"))
    # user_text=message.text
    # await (message.answer(user_text))

@user_router.message(F.text.lower() == "назад")
async def back_menu(message: types.Message):
    await (message.answer("главное меню", reply_markup=reply.main_kb))