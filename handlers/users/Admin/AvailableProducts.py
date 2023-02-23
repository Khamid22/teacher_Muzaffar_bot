from loader import dp, db
from aiogram.types import Message
from keyboards.default.admin_panel import category_keyboard
from keyboards.inline.admin_panel import modify_keyboard
from states.AdminState import OldProducts


@dp.message_handler(text="Available Products")
async def all_existing_products(message: Message):
  await message.answer("Choose one of the categories below", reply_markup=await category_keyboard())
  await OldProducts.all_products.set()


@dp.message_handler(state=OldProducts.all_products)
async def list_products(message: Message):
  category = message.text
  products = await db.get_products(category)
  for product in products:
    photo = product.get("photo")
    text = f"Name: {product.get('product_name')}\n"
    text += f"Price: {product.get('price')} сум"
    await message.answer_photo(photo,text, reply_markup=modify_keyboard)
