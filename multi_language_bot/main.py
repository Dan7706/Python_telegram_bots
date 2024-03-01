import config
from translate import _
from aiogram import Bot, Dispatcher

TOKEN = "YOUR_BOT_TOKEN_HERE"

bot = Bot(config.BOT_TOKEN)
dp = Dispatcher(bot)

user_language = {"user_id": "user_language"}



@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id in user_language.keys():
            await bot.send_message(message.from_user.id, f"{_('Successfull registration!, user_language.get(message.from_user.id))}")
        else:
            await bot.send_message(user_id, "Выберите язык:🇷🇺\nChoose a Language:🇺🇲", reply_markup=nav.lang_menu)



@dp.message_handler()
async def echo(message: types.Message):
    if message.chat.type == "private":
        await bot.send_message(message.from_user.id, f"You have sent {message.text} message!")



@dp.callback_query_handler(text_contains="lang_")
async def set_language(callback: types.CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    lang = callback.data.split("_")[-1]
    global user_language
    #add a new key-value pain to the dictionary using subscript notation.
    user_language[callback.from_user.id] = lang
    await bot.send_message(callback.from_user.id, f"{_('Successful registration!', lang)}")




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


