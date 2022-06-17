from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from data_base import sqlite_db


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛСБ напишите ему:\nhttps://t.me/Pizzza_MasterBot')


# @dp.message_handler(commands=['Режим работы'])
async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Пн-Сб с 9:00 до 20:00, Вс с 10:00 до 21:00')


# @dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул.Ленина 12')


@dp.message_handler(commands=['Меню'])
async def pizza_menu_command(message : types.Message):
    await sqlite_db.sql_read(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['Режим_работы'])
    dp.register_message_handler(pizza_place_command, commands=['Расположение'])
    dp.register_message_handler(pizza_menu_command, commands=['Меню'])