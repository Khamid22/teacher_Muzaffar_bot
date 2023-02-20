from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message
from keyboards.default.admin_panel import admin_menu_keyboard, products_keyboard
from data.config import ADMINS
from loader import dp


@dp.message_handler(CommandStart(), user_id=ADMINS)
async def start_bot(message: Message):
  await message.answer("Admin Panel is activated, how can I help you today?", reply_markup=admin_menu_keyboard)


@dp.message_handler(text="Products")
async def modify_products(message: Message):
  await message.answer("Products Menu", reply_markup=products_keyboard)
