from telegram import update
import logging
from aiogram import Bot, Dispatcher, executor, types
from requests import get
from random import randint


logging.basicConfig(level=logging.INFO, filename="Seminar31.01.2023_dz\Bot\log.csv", filemode="a",
                    format="%(asctime)s: %(levelname)s %(funcName)s-%(lineno)d %(message)s")

bot = Bot("6014640823:AAECK3o5pn-0uSQ36U6Y9vuZqHLjDQTqV94")
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    user_bot = message.from_user.is_bot
    user_message = message.text
    logging.info(f'{user_id=} {user_bot=} {user_message=}')
    await message.reply(f"Hi, {user_full_name}!")
    btns = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn_cats = types.KeyboardButton('/cats')
    btn_exit = types.KeyboardButton('/exit')
    btns.add(btn_cats, btn_exit)
    await bot.send_message(user_id, 'Сделайте выбор', reply_markup=btns)


@dp.message_handler(commands=['exit'])
async def exit(message: types.Message):
    user_full_name = message.from_user.full_name
    await bot.send_message(message.from_user.id, f'GoodBye! {user_full_name}',
                           reply_markup=types.ReplyKeyboardRemove())
    

@dp.message_handler(commands=['cats'])
async def cats(message: types.Message):
    num = randint(1, 1000)
    source = get(f"https://aws.random.cat/view/{num}").text
    await bot.send_message(message.from_user.id, source.split("src=\"")[1].split("\"")[0])


if __name__ == '__main__':
    executor.start_polling(dp)
