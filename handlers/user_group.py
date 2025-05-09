from aiogram import types, Router, F

group_router=Router()

restricted_words=["фейк", "обман", "экзамены"]


@group_router.message(F.text)
async def words_list(message: types.Message):
    words_lst = message.text.lower().split(" ")
    for word in words_lst:
        if word in restricted_words:
            await (message.answer(f"{message.from_user.first_name}, соблюдайте правила чата"))
            await message.delete()
            break