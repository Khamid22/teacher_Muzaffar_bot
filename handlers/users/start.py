import asyncpg.exceptions
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, db, bot
from keyboards.default.menu import phone_number
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
  await message.answer(f"Hi,{message.from_user.full_name} !, please send your phone number", reply_markup=phone_number)

  count = await db.count_users()
  msg = f"{user[1]} has been added to the database.\nNumber of users: {count}."
  await bot.send_message(chat_id=ADMINS[0], text=msg)


@dp.message_handler(content_types=['contact'])
async def get_phone(message: types.Message):
    await db.update_user_number(int(message.contact.phone_number), message.from_user.id)
    await message.answer("Welcome to our online cafe!")