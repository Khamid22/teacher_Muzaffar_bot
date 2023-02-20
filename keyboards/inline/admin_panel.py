from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


def keyboard(page_number):
  prev_button = InlineKeyboardButton("<< Prev", callback_data=f"customer_list_page_{page_number - 1}")
  next_button = InlineKeyboardButton("Next >>", callback_data=f"customer_list_page_{page_number + 1}")
  return InlineKeyboardMarkup().add(prev_button, next_button)