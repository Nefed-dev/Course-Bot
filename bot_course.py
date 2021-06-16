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

# TODO Переместить
@dp.message_handler(Command('help'))
async def help_message(message: Message):
    await message.answer(text='Привет, если возникли какие-то проблемы с ботом или видеоуроками, '
                              'то напиши мне в телеграм @nfd_admin')

# TODO Переместить
@dp.message_handler(Command('start'))
async def start_message(message: Message):
    await message.answer(text=f'{content.MESSAGES["start"]}',
                         reply_markup=Keyboard().phone_request())
    print(db.all_phone())


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

# TODO Переместить
@dp.message_handler(Command('sendall', prefixes='!'))
async def admin_send_all(message: types.Message):
    user_id = message.from_user.id
    if user_id in ADMIN_ID:
        print(db.all_id_users())
        for id in db.all_id_users():
            try:
                print(id[0])
                await bot.send_message(chat_id=id[0], text=message.text[8:])
                await sleep(0.3)
            except Exception as exc:
                print(exc)

# TODO Переместить
@dp.message_handler(Command('refresh', prefixes='!'))
async def refresh(message: types.Message):
    user_id = message.from_user.id
    await bot.delete_message(message_id=message.message_id, chat_id=message.chat.id)
    if user_id in ADMIN_ID:
        for id in db.all_id_users():
            try:
                print(id[0])
                await bot.send_message(chat_id=id[0],
                                       text=message.text[8:],
                                       reply_markup=Keyboard().all_modules(content.MODULE_NAME))
                await sleep(0.3)
            except Exception as exc:
                print(exc)


@dp.callback_query_handler(text_contains='show_all_modules')
async def back_to_modules(query: CallbackQuery):
    await bot.delete_message(message_id=query.message.message_id, chat_id=query.message.chat.id)
    await query.message.answer(text=content.MESSAGES['module_selection'],
                               reply_markup=Keyboard().all_modules(module_dict=content.MODULE_NAME))


@dp.callback_query_handler(text_contains='module_')
async def exercise_keyboard(query: CallbackQuery):
    await bot.delete_message(message_id=query.message.message_id, chat_id=query.message.chat.id)
    await query.message.answer(text=f'{content.MODULE_NAME[query.data]}'
                                    f'\n\n'
                                    f'Выбери номер задания из ОГЭ, которое будешь разбирать 👇🏻',
                               reply_markup=Keyboard().exercise_in_module(exercise_dict=content.module[query.data]))


@dp.callback_query_handler(text_contains='_exercise_')
async def lessons_keyboard(query: CallbackQuery):
    mod = f'{query.data[1]}'
    await bot.delete_message(message_id=query.message.message_id, chat_id=query.message.chat.id)
    await query.message.answer(text=f'{content.EXERCISE_NAME[query.data[3:]]}\n\nА теперь выбери урок 👇🏻',
                               reply_markup=Keyboard().lessons(lessons_dict=content.exercise[query.data], module=mod))


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
