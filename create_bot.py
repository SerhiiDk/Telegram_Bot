from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
bot = Bot(token="5056403449:AAEIt0g76m7qrT9h_cscn1BOkslivullpoM")
dp = Dispatcher(bot, storage=storage)
