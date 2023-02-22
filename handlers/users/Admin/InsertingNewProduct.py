from handlers.users.Admin.AdminPanel import start_bot
from loader import dp, db
from aiogram import types
from keyboards.inline.admin_panel import keyboard
from aiogram.types import Message, CallbackQuery
from keyboards.default.admin_panel import back
from aiogram.dispatcher import FSMContext
from states.AdminState import NewProduct


@dp.message_handler(text="Add new product")
async def send_photo_command(message: Message):
  await message.answer("Send a photo: ", reply_markup=back)
  await NewProduct.waiting_for_photo.set()


@dp.message_handler(content_types=types.ContentType.PHOTO, state=NewProduct.waiting_for_photo)
async def process_photo(message: Message, state: FSMContext):
  photo = message.photo[-1].file_id
  await state.update_data(
    {"photo": photo}
  )
  await message.answer("<b>Enter a name </b>")
  await NewProduct.waiting_for_name.set()


@dp.message_handler(state=NewProduct.waiting_for_name)
async def product_name(message: Message, state: FSMContext):
  name = message.text
  await state.update_data(
    {"name": name}
  )
  await message.answer("<b>Enter the price\nExample: 10000 (only integers)</b>")
  await NewProduct.waiting_for_price.set()


@dp.message_handler(state=NewProduct.waiting_for_price)
async def set_price(message: Message, state: FSMContext):
  price = int(message.text)
  await state.update_data(
    {"price": price}
  )
  await message.answer("<b>name the category:</b>")
  await NewProduct.waiting_for_category_name.set()


@dp.message_handler(state=NewProduct.waiting_for_category_name)
async def set_category(message: Message, state: FSMContext):
  category_name = message.text
  await state.update_data({"category_name": category_name})
  data = await state.get_data()
  photo = data.get("photo")
  name = data.get("name")
  price = data.get("price")
  category_name = data.get("category_name")

  msg = "New product📝: \n"
  msg += f"Name - {name}\n"
  msg += f"Price - {price} сум\n"
  msg += f"Category - {category_name}\n"

  async with state.proxy() as proxy:
    proxy['name'] = name
    proxy['price'] = price
    proxy['category'] = category_name
    proxy['photo'] = photo
  await message.reply_photo(photo, msg, reply_markup=keyboard)
  await NewProduct.confirm.set()


@dp.callback_query_handler(state=NewProduct.confirm)
async def process_callback_button(call: CallbackQuery, state: FSMContext):
  data = call.data
  if data == "done":
    async with state.proxy() as proxy:
      name = proxy.get('name')
      price = proxy.get('price')
      category_name = proxy.get('category')
      photo = proxy.get('photo')
      await db.add_product(category_name, name, photo, price)
    if category_name and name:
      await call.answer(f"{name} has been added to the category of {category_name}", show_alert=True)
    else:
      await call.answer("Error: missing data.")
  elif data == "cancel":
    await call.answer(f"The process has been cancelled", show_alert=True)
  await call.message.delete()
  await start_bot(call.message)
  await state.finish()


@dp.message_handler(text="back", state="*")
async def back_main_menu(message: Message, state:FSMContext):
  await start_bot(message)
  await state.finish()
