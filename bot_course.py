from asyncio import sleep
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery, Message
from database import Database
from keyboard import Keyboard

from data import config

import content
import keyboard

BOT_TOKEN = config.BOT_TOKEN
ADMIN_ID = [1782255380, ]

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)
db = Database(path_to_db='course_students.db')


# TODO Переместить
async def set_default_commands(dp):
    await dp.bot.set_my_commands([types.BotCommand("start", 'Запустить бота'), types.BotCommand("help", 'Памагити')])


# TODO Переделать
@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def check_phone(message: Message):
    user_id = message.from_user.id
    phone_number = message.contact.phone_number
    db.update_user_id(phone=phone_number, id=user_id)
    tariff = db.check_tariff_plan(user_id)
    print(phone_number)

    for number in db.all_phone():
        if phone_number in number:
            await message.answer(text=f"{content.reg_ok(tariff)}",
                                 reply_markup=keyboard.ReplyKeyboardRemove())
            await message.answer(text=content.MESSAGES['module_selection'],
                                 reply_markup=Keyboard().all_modules(content.MODULE_NAME))


@dp.callback_query_handler(text_contains='_exc')
async def send_homework(query: CallbackQuery):
    def check_list(tariff, lesson):
        if tariff[0] == 'basic':
            return ''

        return f'Рабочая тетрадь к уроку: {lesson["workbook"]}' \
               f'\n\n' \
               f'Чек-лист к уроку: {lesson["check_list"]}' \
               f'\n\n' \
               f'Шпаргалка с формулами: {lesson["cheatsheet"]}\n\n'

    user_id = query.from_user.id
    tariff = db.check_tariff_plan(user_id)
    exc = f'{query.data[:2]}_exercise_{query.data[-5:-3]}'
    mod = f'{query.data[1]}'
    lesson = content.exercise[exc][query.data]
    print(query.data[1])
    await bot.delete_message(message_id=query.message.message_id, chat_id=query.message.chat.id)
    await query.message.answer(text=f'Теоретический урок: {lesson["link"]}'
                                    f'\n\nПрактический урок: {lesson["practice"]}'
                                    f'\n\n{check_list(tariff, lesson)}'
                                    f'Твоя домашка: {lesson["homework"]}',
                               reply_markup=Keyboard().lessons(lessons_dict=content.exercise[exc], module=mod))


async def on_startup(dp):
    await set_default_commands(dp)


if __name__ == '__main__':
    try:
        executor.start_polling(dp, on_startup=on_startup)
    except Exception as err:
        print(err)
