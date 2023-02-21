from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from loader import dp, db
from states.ordering import OrderData
from geopy.geocoders import Nominatim
import re
from keyboards.default.menu import get_phonenum


# @dp.message_handler(Command("location"), state=None)
# async def begin(message: types.Message):
#     await message.answer("📍 send your location", reply_markup=save_location())
#     await OrderData.location.set()


@dp.message_handler(content_types="location", state=OrderData.location)
async def get_location(message: types.Message, state: FSMContext):
    lat = message.location.latitude
    lon = message.location.longitude
    geolocator = Nominatim(user_agent="timur2003qodirov@gmail.com")
    geolocation = geolocator.reverse(str(lat)+", " + str(lon))
    # location =
    await message.answer(geolocation)
    await message.answer("your phone number", reply_markup=get_phonenum())
    await OrderData.phone.set()


@dp.message_handler(state=OrderData.phone)
async def get_phone(message: types.Message, state: FSMContext):
    contact = message.contact.phone_number
    await message.answer(message.text)
    await OrderData.categories.set()


@dp.message_handler(state=OrderData.categories)
async def categories(message: types.Message):
    await message.answer("2")

