"""
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message
from keyboards.default.menu import admin_menu_keyboard
from data.config import ADMINS
from loader import dp


@dp.message_handler(CommandStart(), user_id=ADMINS)
async def start_bot(message: Message):
  await message.answer("Admin Panel is activated", reply_markup=admin_menu_keyboard)

@dp.message_handler(text="users")
async def show_user(message: Message):
"""