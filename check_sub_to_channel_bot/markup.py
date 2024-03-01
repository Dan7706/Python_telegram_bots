from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

button1 = InlineKeyboardButton('SUBSCRIBE', url="https://t.me/your_telegram_channel_link")
button2 = InlineKeyboardButton('CHECK SUBSCRIBTION', callback_data="subToChannel")

sub_menu = InlineKeyboardMarkup(row_width=1)
sub_menu.add(buttonProfile)
