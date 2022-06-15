from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

async def on_startup(_):
    print('Бот вышел в онлайн')

'''***client side***'''

@dp.message_handler(commands=['start','help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита')
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛСБ напишите ему:\nhttps://t.me/Pizzza_MasterBot')

@dp.message_handler(commands=['Режим работы'])
async def pizza_open_command(message : types.Message):
    await bot.send_message(message.from_user_id, 'Пн-Сб с 9:00 до 20:00, Вс с 10:00 до 21:00')

@dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message : types.Message):
    await bot.send_message(message.from_user_id, 'ул.Ленина 12')

# @dp.message_handler(commands=['Меню'])
# async def pizza_menu_command(message : types.Message):
#   for ret in cur.execute('SELECT * FROM menu').fetchall():
#       await bot.send_photo(message.from_user_id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')

'''***admin side***'''



'''***general side***'''


@dp.message_handler()
async def echo_send(message : types.Message):
    if message.text == 'Привет':

        await message.answer('И тебе привет')
    await message.reply(message.text)
    await bot.send_message(message.from_user.id, message.text)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)