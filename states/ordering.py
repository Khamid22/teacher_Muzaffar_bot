from aiogram.dispatcher.filters.state import StatesGroup, State


class OrderData(StatesGroup):
    location = State()
    categories = State()
    product = State()
    final = State()
    backet = State()
