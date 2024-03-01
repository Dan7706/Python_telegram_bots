from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


lang_menu = InlineKeyboardMarkup(row_width=2)
langRU = InlineKeyboardButton(text="🇷🇺Русский", callback_data="lang_ru")
langEN = InlineKeyboardButton(text="🇺🇲English", callback_data="lang_en")
lang_menu.insert(langRU)
lang_menu.insert(langEN)


