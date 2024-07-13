import logging
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import config
from RandomFox import fox
from keyboards import kb1, kb2
from random import randint
API_TOKEN = config.token

# Включаем логирование, чтобы видеть сообщения в консоли
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

#команда старт
@dp.message(Command("start"))
async def command_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Привет, {name}', reply_markup=kb1)

#команда help
@dp.message(Command("help"))
async def send_ura(message: types.Message):
    await message.answer("Это бот созданн в виде домашнего задания на курсе Нейрохищник. Можете воспользоваться командами /start, /help, /about")

#команда about
@dp.message(Command("about"))
async def send_ura(message: types.Message):
    await message.answer("Пока я могу присылать Вам то, что Вы напишите, отправлять милую лисичку.")

#команда лисы
@dp.message(Command("fox"))
@dp.message(Command("лиса"))
async def send_fox(message: types.Message):
    image_fox = fox()
    # await message.answer_photo(image_fox)
    await bot.send_photo(message.chat.id, image_fox)
    # await message.answer(f"{image_fox}")

#хендлер на сообщения
@dp.message(F.text.lower)
async def msg_echo(message: types.Message):
    msg_user = message.text.lower()
    name = message.chat.first_name
    if 'привет' in msg_user:
        await message.answer(f'Приветствую, {name}')
    elif 'пока' in msg_user:
        await message.answer(f'Пришло время прощаться, {name}')
    elif 'как дела' in msg_user:
        await message.answer(f'У нас всё нормально, нормально нереально, {name}')
    elif 'ты кто' in msg_user:
        await message.answer(f'Я чат бот, созданный в качестве домашнего задания, {name}')
    elif 'меню' in msg_user:
        await message.answer(f'Смотри, что у меня есть! {name}', reply_markup=kb1)
    else:
        await message.answer(f'Неизвестная команда!')


@dp.message()
async def echo(message: types.Message):
    if "ура" in message.text:
        await message.answer("УРАААА!")
    elif message.text == "инфо":

        user_name = message.chat.id
        print(user_name)
        await message.answer(str(user_name))
    else:
        await message.answer(message.text)




async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())