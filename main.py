import asyncio
from aiogram import Bot, Dispatcher


TOKEN="7803896890:AAFol5p5huJZ3b7bkPJCgBKOebZ3w0i0vcU"

bot = Bot(token = TOKEN)
dp = Dispatcher()

from handlers.user_private import user_router
from handlers.user_group import group_router

dp.include_router(user_router)
dp.include_router(group_router)


async def main():
    print("бот запущен")
    await dp.start_polling(bot)


asyncio.run(main())