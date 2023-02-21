from aiogram.dispatcher.filters.state import StatesGroup, State


class NewProduct(StatesGroup):
  waiting_for_photo = State()
  waiting_for_name = State()
  waiting_for_price = State()
  waiting_for_category_name = State()
  waiting_for_subcategory_name = State()
  confirm = State()