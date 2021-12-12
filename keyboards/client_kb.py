from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Work_time')
b2 = KeyboardButton('/Location')
b3 = KeyboardButton('/Menu')
# b4 = KeyboardButton('/Поделыться номером', request_contact=True)
# b5 = KeyboardButton('/Отправить где я', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)  # one_time_keyboard=True - одноразовость

kb_client.add(b1).add(b2).insert(b3)  # .row(b4, b5)

# kb_client.row(b1, b2, b3, b4, b5)

# kb_client.add(b1).add(b2).insert(b3, b4, b5)
