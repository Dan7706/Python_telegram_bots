import time

import markup as nav
from db import Database

from aiogram import Bot, Dispatcher, executor, types



TOKEN = "YOUR_TOKEN_HERE"


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
db = Database("database.db")


def check_subscription(chat_member):
    if chat_member["status"] != "left" and chat_member['status'] != "kicked":
        return True
    else:
        return False


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    if (not db.user_exists(message.from_user.id)):
        db.add_user(message.from_user.id)
    if check_subscription(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
        await bot.send_message(message.from_user.id, f"Hello {}\nYou have successfully subscribes to our channel!\nWelcome to our bot!")
    else:
        await bot.send_message(message.from_user.id, "In Order To Use This Bot You Have To Subscribe To The Channel!", reply_markup=nav.sub_menu)


@dp.message_handler()
async def echo_message(message: types.Message):
    if message.chat.type == "private":
        if check_subscription(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
            await bot.send_message(message.from_user.id, f"You have sent message: {message.text}")
        else:
            await bot.send_message(message.from_user.id, "In Order To Use This Bot You Have To Subscribe To The Channel!", reply_markup=nav.sub_menu)




@dp.callback_query_handler(text="subToChannel")
async def subToChannel(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    if check_subscription(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
        await bot.send_message(message.from_user.id, f"Hello {}\nYou have successfully subscribes to our channel!\nWelcome to our bot!")
    else:    
        await bot.send_message(message.from_user.id, "In Order To Use This Bot You Have To Subscribe To The Channel!", reply_markup=nav.sub_menu)





if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
