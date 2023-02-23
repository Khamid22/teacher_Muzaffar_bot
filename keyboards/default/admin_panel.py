from aiogram.types.reply_keyboard import KeyboardButton, ReplyKeyboardMarkup
from loader import db

admin_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
admin_btns_text = ("Products", "Customers")
for text in admin_btns_text:
  admin_menu_keyboard.add(KeyboardButton(text))

products_keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
options = ("Available Products", "Add new product", "back")
for option in options:
  products_keyboard.add(option)

back = ReplyKeyboardMarkup(resize_keyboard=True)
text = "back"
back.add(text)


async def category_keyboard():
  keyboard = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
  categories = await db.get_categories()
  for category in categories:
    button_text = f"{category}"
    keyboard.add(button_text)
  keyboard.add(text)
  return keyboard

