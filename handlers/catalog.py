from aiogram import types, Router, F
from aiogram.types import FSInputFile

catalog_router=Router()

@catalog_router.message(F.text.lower() == ("colonwell"))
async def first_product(message: types.Message):
    photo=FSInputFile("img/catalog/colonwell.jpg")
    await message.answer_photo(photo, caption="ColonWell")
    await (message.answer("""ColonWell - Здоровый кишечник - полностью натуральный растительный продукт для взрослых и детей. Поддерживает нормальную функцию кишечника и вызывает сытость."
100% органический, без глютена, сои, без молочных продуктов и без ГМО. Подходит для вегетарианцев и веганов.
ColonWell идеально подходит для:
- эффективного естественного и полезного снижения веса
- поддержания нормальной функции кишечника и ЖКТ
- поддержания нормального уровня холестерина в крови
- гигиены кишечника."""))

@catalog_router.message(F.text.lower() == ("colonwell active"))
async def first_product(message: types.Message):
    photo=FSInputFile("img/catalog/colonwell_active.jpg")
    await message.answer_photo(photo, caption="ColonWell Active")
    await (message.answer("""ColonWell Active - Здоровый кишечник - полностью натуральный растительный продукт для взрослых и детей. Поддерживает нормальную функцию кишечника и вызывает сытость."
100% органический, без глютена, сои, без молочных продуктов и без ГМО. Подходит для вегетарианцев и веганов.
ColonWell Active идеально подходит для: 
- эффективного естественного и полезного снижения веса
- поддержания нормальной функции кишечника и ЖКТ
- поддержания нормального уровня холестерина в крови
- гигиены кишечника."""))

@catalog_router.message(F.text.lower() == ("colonwell prolentan"))
async def first_product(message: types.Message):
    photo=FSInputFile("img/catalog/prolentan.jpg")
    await message.answer_photo(photo, caption="ColonWell Prolentan")
    await (message.answer("""ColonWell Prolentan - Здоровый кишечник - полностью натуральный растительный продукт для взрослых и детей. Поддерживает нормальную функцию кишечника и вызывает сытость.
100% органический, без глютена, сои, без молочных продуктов и без ГМО. Подходит для вегетарианцев и веганов.
ColonWell идеально подходит для:
- эффективного естественного и полезного снижения веса
- поддержания нормальной функции кишечника и ЖКТ
- поддержания нормального уровня холестерина в крови
- гигиены кишечника."""))

@catalog_router.message(F.text.lower() == ("tricollagen peptide"))
async def first_product(message: types.Message):
    photo=FSInputFile("img/catalog/peptid.jpg")
    await message.answer_photo(photo, caption="TriCollagen Peptide")
    await (message.answer("""TriCollagen Peptide - коллаген в жидком виде, содержащий 3 основные группы биологически-активных компонентов. 
В составе содержится коллаген, полученный из рыбы, который является одним из наиболее важных белков в организме.
Коллаген присутствует в коже, костях, хрящах, сухожилиях, связках, мышцах, а также в зубах и  деснах, роговице, кровеносных сосудах, внутренних органах и тканях."""))

@catalog_router.message(F.text.lower() == ("tricollagen microhyaluron"))
async def first_product(message: types.Message):
    photo=FSInputFile("img/catalog/micro.jpg")
    await message.answer_photo(photo, caption="TriCollagen MicroHyaluron")
    await (message.answer("""FenoQ MicroHyaluron рекомендуется употреблять сразу после дозы FenoQ TriCollagen Peptide,
тем самым обеспечивая высокоэффективное восстановление влаги кожи и инъекцию омоложения без каких-либо игл и пластических хирургов!"""))