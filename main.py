import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode



TOKEN="7803896890:AAFol5p5huJZ3b7bkPJCgBKOebZ3w0i0vcU"

bot = Bot(token = TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

from handlers.user_private import user_router
from handlers.user_group import group_router
from handlers.catalog import catalog_router

dp.include_router(user_router)
dp.include_router(catalog_router)
dp.include_router(group_router)


async def main():
    print("бот запущен")
    await dp.start_polling(bot)


asyncio.run(main())