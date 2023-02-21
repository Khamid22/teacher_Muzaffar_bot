from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from loader import dp, db
from states.ordering import OrderData
from geopy.geocoders import Nominatim



@dp.message_handler(state=OrderData.categories)
async def categories(message: types.Message):
    await message.answer("2")

