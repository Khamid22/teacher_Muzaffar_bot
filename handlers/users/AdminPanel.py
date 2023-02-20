from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import Message
from aiogram.dispatcher.filters import CommandStart
from keyboards.default.admin_panel import admin_menu_keyboard, products_keyboard
from data.config import ADMINS
from loader import dp, db


@dp.message_handler(CommandStart(), user_id=ADMINS)
async def start_bot(message: Message):
  await message.answer("Admin Panel is activated, how can I help you today?", reply_markup=admin_menu_keyboard)


@dp.message_handler(text="Products")
async def modify_products(message: Message):
  await message.answer("Products Menu", reply_markup=products_keyboard)


@dp.message_handler(text="Customers")
async def show_all_customers(message: Message):
  customers = await db.select_all_users()
  page_size = 10
  page_number = 1
  if not customers:
    await message.answer("<b>No registered customers.</b>")
  else:
    start_index = (page_number - 1) * page_size
    end_index = start_index + page_size
    paginated_customers = customers[start_index:end_index]
    customer_list = ""
    # Define the number of customers per page
    for customer in paginated_customers:
      customer_number = customer.get("id")
      name = customer.get("full_name")
      username = customer.get("username")
      phone_number = customer.get("phone_number")
      customer_list += f"<b>Customer #{customer_number}</b>\n<b>Name: {name}</b>\n<b>Username: @{username} </b>\n " \
                       f"<b>Phone: {phone_number}</b>\n\n "

    # Create the page turning buttons
    prev_button = InlineKeyboardButton(
      "<< Prev",
      callback_data=f"customer_list_page_{page_number - 1}"
    )
    next_button = InlineKeyboardButton(
      "Next >>",
      callback_data=f"customer_list_page_{page_number + 1}"
    )
    keyboard = InlineKeyboardMarkup().add(prev_button, next_button)
    await message.answer(customer_list, reply_markup=keyboard)




