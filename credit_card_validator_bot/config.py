from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    full_name =  message.from_user.full_name
    user_id = message.from_user.id
    await bot.send_message(user_id, f"Hello dear {full_name}.\nThis bot helps people 
                           to validate credit card numbers.\nSend any credit/debit card number to the bot 
                           and it will give you a proper answer whether the number is VALID or INVALID.
                           Thanks for using our bot!")



@dp.message_handler()
async def all_messages(message: types.Message):
    card_number = message.text
    user_id = message.from_user.id
    
    if not card_number.isdigit():
        await bot.send_message(user_id, f"I am sorry! {card_number} card number you entered is not a proper one.\n
                               Card number should contain only numbers 0-9.\n
                               Thanks for using our bot!")
    
    else:
        sum_odd_digits = sum_even_digits = total = 0
        card_number = card_number[::-1]

        for x in card_number[::2]:
            sum_odd_digits += int(x)


        for x in card_number[1::2]:
            x = int(x) * 2
            if x >= 10:
                sum_even_digits += (1 + (x % 10))
            else:
                sum_even_digits += x


        total = sum_odd_digits + sum_even_digits


        if total % 10 == 0:
            await bot.send_message(user_id, f"{card_number} card number is VALID!\n\n
                                   Thank you for using our bot!")
        else:
            await bot.send_message(user_id, f"{card_number} card number is INVALID!\n\n
                                   Thank you for using our bot!")




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
