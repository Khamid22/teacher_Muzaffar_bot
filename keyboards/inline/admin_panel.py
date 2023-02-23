from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboard = InlineKeyboardMarkup(row_width=2)
keyboard.insert(InlineKeyboardButton("Done", callback_data="done"))
keyboard.insert(InlineKeyboardButton("Cancel", callback_data="cancel"))

modify_keyboard = InlineKeyboardMarkup(row_width=2)
modify_keyboard.insert(InlineKeyboardButton("Edit", callback_data="edit"))
modify_keyboard.insert(InlineKeyboardButton("Delete", callback_data="delete"))
