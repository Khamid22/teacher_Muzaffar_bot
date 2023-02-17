from aiogram.types.reply_keyboard import KeyboardButton, ReplyKeyboardMarkup

# Admin menu keyboards
admin_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
admin_btns_text = ("Users", "Account")
for text in admin_btns_text:
  admin_menu_keyboard.add(KeyboardButton(text))

# ordinary user
menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
btns_text = ("Vocabulary", "Dictionary", "About us")
for text in btns_text:
  menu_keyboard.add(KeyboardButton(text))
