print ("Hello")
import asyncio
from aiogram import Bot, Dispatcher, types
TOKEN="7803896890:AAFol5p5huJZ3b7bkPJCgBKOebZ3w0i0vcU"
bot=Bot(token=TOKEN)
dp=Dispatcher()
async def main():
    print ("async")
    await dp.start_polling(bot)
asyncio.run(main())