from aiogram import types

#создание кнопок
button1 = types.KeyboardButton(text='/start')
button2 = types.KeyboardButton(text='/help')
button3 = types.KeyboardButton(text='/about')
button4 = types.KeyboardButton(text='/fox')
button5 = types.KeyboardButton(text='Закрыть')

#раскладка кнопок
keyboard1 = [
[button1, button2, button3],
[button4, button5]
]

keyboard2 = [
[button1, button2, button3],
]

kb1 = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)
kb2 = types.ReplyKeyboardMarkup(keyboard=keyboard2, resize_keyboard=True)