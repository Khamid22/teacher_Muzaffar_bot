from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from loader import dp
from states.ordering import OrderData
from geopy.geocoders import Nominatim

def get_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton("Share Position", request_location=True)
    keyboard.add(button)
    return keyboard


@dp.message_handler(Command("location"), state=None)
async def begin(message: types.Message):
    await message.answer("📍 send your location", reply_markup=get_keyboard())
    await OrderData.location.set()


@dp.message_handler(content_types="location", state=OrderData.location)
async def get_location(message: types.Message):
    lat = message.location.latitude
    lon = message.location.longitude
    geolocator = Nominatim(user_agent="timur2003qodirov@gmail.com");
    location = geolocator.reverse(str(lat)+", " + str(lon))

    await message.answer(location)
