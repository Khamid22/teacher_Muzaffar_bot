from aiogram.types.reply_keyboard import KeyboardButton, ReplyKeyboardMarkup

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
