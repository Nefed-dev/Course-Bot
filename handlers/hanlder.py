# На "старт" предложить регистрацию с запросом номера телефона
from bot_course import dp
from aiogram import types
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Command

from db_commands import get_item
from keyboards import keyboards as kb


@dp.message_handler(Command('start'))
async def bot_start(message: Message):
    """
    Приветственная клавиатура, запрос номера телефона у пользователя
    """
    await message.answer(text='Hello message + Phone-request keyboard',
                         reply_markup=kb.phone_request_keyboard())


@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def check_phone(message: Message):
    # TODO прописать проверку наличия номера телефона в БД с помощью регулярного выражения
    # TODO Дополнение данными базы данных - user_id, если номер телефона присутствует в БД

    markup = await kb.categories_keyboard()
    await message.edit_reply_markup(markup)


async def list_categories(query: CallbackQuery):
    markup = await kb.categories_keyboard()
    await query.message.edit_reply_markup(markup)


async def list_subcategories(query: CallbackQuery, category, **kwargs):
    markup = await kb.subcategories_keyboard(category)
    await query.message.edit_reply_markup(markup)


async def list_item(query: CallbackQuery, category, subcategory, **kwargs):
    markup = await kb.items_keyboard(category, subcategory)
    await query.message.edit_reply_markup(markup)


async def show_item(query: CallbackQuery, category, subcategory, item_id):
    item = await get_item(item_id)
    markup = None
    # TODO Передать клавиатуру со списком из Подкатегории и кнопкой назад
    # TODO Добавить проверку на тариф, отредактировать поле text согласно тарифу
    # TODO Попробовать изменять текст через функцию, как делал это ранее или может попробовать через БД?
    text = f'{item.name}\nHomework: {None}\nCheatsheet: {None}\nCheck-list: {None}'
    await query.message.edit_text(text=text, reply_markup=markup)


@dp.callback_query_handler(kb.menu_cd.filter())
async def navigate(query: CallbackQuery, callback_data: dict):
    current_level = callback_data.get('level')
    category = callback_data.get('category')
    subcategory = callback_data.get('subcategory')
    item_id = callback_data.get('item_id')

    levels = {
        '0': list_categories,
        '1': list_subcategories,
        '2': list_item,
        '3': show_item
    }
    current_level_func = levels[current_level]
    await current_level_func(
        query,
        category=category,
        subcategory=subcategory,
        item_id=item_id
    )
