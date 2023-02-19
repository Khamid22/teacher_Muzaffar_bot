import asyncpg.exceptions
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menu import menu_keyboard
from loader import dp, db, bot
from data.config import ADMINS


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
  try:
    user = await db.add_user(telegram_id=message.from_user.id,
      full_name=message.from_user.full_name,
      username=message.from_user.username,
    )
  except asyncpg.exceptions.UniqueViolationError:
    user = await db.select_user(telegram_id=message.from_user.id)
  await message.answer(f"Hi, {message.from_user.full_name}!", reply_markup=menu_keyboard)

  count = await db.count_users()
  msg = f"{user[1]} has been added to the database.\nNumber of users: {count}."
  await message.answer(text=msg)
