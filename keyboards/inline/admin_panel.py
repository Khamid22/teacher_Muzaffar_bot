from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboard = InlineKeyboardMarkup(row_width=2)
keyboard.insert(InlineKeyboardButton("Done", callback_data="done"))
keyboard.insert(InlineKeyboardButton("Cancel", callback_data="cancel"))
