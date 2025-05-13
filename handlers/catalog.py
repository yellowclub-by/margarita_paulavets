from aiogram import types, Router, F
from aiogram.types import FSInputFile

catalog_router=Router()

@catalog_router.message(F.text.lower() == ("1-й продукт"))
async def first_product(message: types.Message):
    photo=FSInputFile("img/catalog/colonwell.jpg")
    await message.answer_photo(photo, caption="1-й продукт")
    await (message.answer("""ColonWell Active - Здоровый кишечник - полностью натуральный растительный продукт для взрослых и детей. Поддерживает нормальную функцию кишечника и вызывает сытость."
100% органический, без глютена, сои, без молочных продуктов и без ГМО. Подходит для вегетарианцев и веганов.
ColonWell идеально подходит для:
- эффективного естественного и полезного снижения веса
- поддержания нормальной функции кишечника и ЖКТ
- поддержания нормального уровня холестерина в крови
- гигиены кишечника."""))

@catalog_router.message(F.text.lower() == ("2-й продукт"))
async def first_product(message: types.Message):
    photo=FSInputFile("img/catalog/colonwell_active.jpg")
    await message.answer_photo(photo, caption="2-й продукт")
    await (message.answer("""ColonWell Active -  - полностью натуральный растительный продукт для взрослых и детей. Поддерживает нормальную функцию кишечника и вызывает сытость."
100% органический, без глютена, сои, без молочных продуктов и без ГМО. Подходит для вегетарианцев и веганов.
ColonWell Active идеально подходит для: 
- эффективного естественного и полезного снижения веса
- поддержания нормальной функции кишечника и ЖКТ
- поддержания нормального уровня холестерина в крови
- гигиены кишечника."""))

@catalog_router.message(F.text.lower() == ("3-й продукт"))
async def first_product(message: types.Message):
    photo=FSInputFile("img/catalog/prolentan.jpg")
    await message.answer_photo(photo, caption="3-й продукт")
    await (message.answer("""ColonWell Prolentan - Здоровый кишечник - полностью натуральный растительный продукт для взрослых и детей. Поддерживает нормальную функцию кишечника и вызывает сытость.
100% органический, без глютена, сои, без молочных продуктов и без ГМО. Подходит для вегетарианцев и веганов.
ColonWell идеально подходит для:
- эффективного естественного и полезного снижения веса
- поддержания нормальной функции кишечника и ЖКТ
- поддержания нормального уровня холестерина в крови
- гигиены кишечника."""))

@catalog_router.message(F.text.lower() == ("4-й продукт"))
async def first_product(message: types.Message):
    photo=FSInputFile("img/catalog/detox.jpg")
    await message.answer_photo(photo, caption="4-й продукт")
    await (message.answer("""ColonWell Detox - полностью натуральный растительный продукт для взрослых и детей. Поддерживает нормальную функцию кишечника и вызывает сытость. 
В состав входит ANTI PARASITAN COMPLEX® (экстракт черного ореха и порошок сушеных лисичек).
100% органический, без глютена, сои, без молочных продуктов и без ГМО.
ColonWell Detox идеально подходит для:
- эффективного естественного и полезного снижения веса
- поддержания нормальной функции кишечника и ЖКТ
- поддержания нормального уровня холестерина в крови
- гигиены кишечника."""))