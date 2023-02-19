from aiogram import types
from aiogram.dispatcher.filters import Command
from loader import dp, db
from states.ordering import OrderData
from geopy.geocoders import Nominatim
import re
from keyboards.default.menu import save_location


# @dp.message_handler(Command("location"), state=None)
# async def begin(message: types.Message):
#     await message.answer("📍 send your location", reply_markup=save_location())
#     await OrderData.location.set()


@dp.message_handler(content_types="location", state=OrderData.location)
async def get_location(message: types.Message):
    lat = message.location.latitude
    lon = message.location.longitude
    geolocator = Nominatim(user_agent="timur2003qodirov@gmail.com")
    geolocation = geolocator.reverse(str(lat)+", " + str(lon))
    # location =
    await message.answer(geolocation)
