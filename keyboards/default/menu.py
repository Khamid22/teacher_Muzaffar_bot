from aiogram.types.reply_keyboard import KeyboardButton, ReplyKeyboardMarkup


# ordinary user
def menu():
  menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
  btns_text = ("Menu", "Settings", "About us")
  for text in btns_text:
    menu_keyboard.add(KeyboardButton(text))
  return menu_keyboard

def save_location():
  keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
  button = KeyboardButton("Share Position", request_location=True)
  keyboard.add(button)
  return keyboard


phone_number = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton("my contact", request_contact=True)
phone_number.add(button)
