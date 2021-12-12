from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards.client_kb import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Hello', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общения с ботом через ЛС, напишите ему:\nhttps://t.me/pizza_chef32Bot')


# @dp.message_handler(commands=['Режим_роботы'])
async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вс-Чт с 9:00 до 20:00б Пт-Сб с 10:00 до 23:00',
                           reply_markup=kb_client)


# @dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул. Колбасная 15', reply_markup=ReplyKeyboardRemove())


# @dp.message_handler(commands=['Меню'])
async def pizza_menu_command(message: types.Message):
    await sqlite_db.sql_read(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['Work_time'])
    dp.register_message_handler(pizza_place_command, commands=['Location'])
    dp.register_message_handler(pizza_menu_command, commands=['Menu'])
