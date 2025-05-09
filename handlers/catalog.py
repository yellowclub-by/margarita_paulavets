from aiogram import types, Router, F
from aiogram.types import FSInputFile

catalog_router=Router()

@catalog_router.message(F.text.lower() == ("1-й продукт"))
async def first_product(message: types.Message):
    photo=FSInputFile("img/catalog/colonwell.jpg")
    await message.answer_photo(photo, caption="1-й продукт")
    await (message.answer("Colonwell"))

@catalog_router.message(F.text.lower() == ("2 продукт"))
async def first_product(message: types.Message):
    photo=FSInputFile("img/catalog/colonwell_active.jpg")
    await message.answer_photo(photo, caption="2-й продукт")
    await (message.answer("Colonwell Active"))

@catalog_router.message(F.text.lower() == ("3 продукт"))
async def first_product(message: types.Message):
    photo=FSInputFile("img/catalog/prolentan.jpg")
    await message.answer_photo(photo, caption="3-й продукт")
    await (message.answer("Colonwell Prolentan"))

@catalog_router.message(F.text.lower() == ("4 продукт"))
async def first_product(message: types.Message):
    photo=FSInputFile("img/catalog/detox.jpg")
    await message.answer_photo(photo, caption="4-й продукт")
    await (message.answer("Colonwell Detox"))
