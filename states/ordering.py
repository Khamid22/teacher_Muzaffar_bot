from aiogram.dispatcher.filters.state import StatesGroup, State


class OrderData(StatesGroup):
    phone = State()
    categories = State()
    sub_categories = State()
    product = State()
    basket = State()

























