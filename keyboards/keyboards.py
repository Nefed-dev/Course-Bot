# Клавиатура с меню-навигацией по курсу
# |--------------------------------------|
# |categories -> subcategories -> items  |
# |module     -> exercise      -> lesson |
# |--------------------------------------|
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
from db_commands import get_categories, get_subcategories, count_items, get_items


def phone_request_keyboard():
    markup = ReplyKeyboardMarkup()
    button_text = 'Press to check registration 📱'
    button = KeyboardButton(text=button_text, request_contact=True)
    markup.add(button)
    return markup


menu_cd = CallbackData('show_menu', 'level', 'module', 'exercise', 'lesson_id')


def make_callback_data(level, categories=0, subcategories=0, item_id=0):
    """Формирование CallbackData для каждого элемента меню, в зависимости от переданных параметров
    Если Модуль или Упражнение не переданы - они по умолчанию равны нулю
    """
    return menu_cd.new(level=level, categories=categories, subcategories=subcategories, item_id=item_id)


async def categories_keyboard():
    # Клавиатура 1 уровня - Categories -> Модули
    CURRENT_LEVEL = 0
    markup = InlineKeyboardMarkup()
    categories = await get_categories()
    for category in categories:
        number_of_items = await count_items(modules.module_code)
        button_text = f'{categories.category_name} ({number_of_items} уроков)'
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1,
                                           categories=categories.category_code)
        markup.insert(InlineKeyboardButton(text=button_text,
                                           callback_data=callback_data))
    return markup


async def subcategories_keyboard(category):
    # Клавитура 2 уровня - Subcategories -> Упражнения
    CURRENT_LEVEL = 1
    markup = InlineKeyboardMarkup()
    subcategories = await get_subcategories(category)
    for subcategory in subcategories:
        number_of_items = await count_items(subcategory)
        button_text = f'{subcategories.subcategories_name} ({number_of_items} уроков)'
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1,
                                           categories=category,
                                           subcategories=subcategory.subcategory_code)
        markup.insert(
            InlineKeyboardButton(text=button_text,
                                 callback_data=callback_data)
        )
    markup.row(InlineKeyboardButton(text='Назад',
                                    callback_data=make_callback_data(level=CURRENT_LEVEL - 1)))
    return markup


async def items_keyboard(category, subcategory):
    # Клавиатура 3 уровня - Items -> Уроки
    CURRENT_LEVEL = 2
    markup = InlineKeyboardMarkup(row_width=1)
    items = await get_items()
    for item in items:
        button_text = f'{item.name}'
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1,
                                           categories=category,
                                           subcategories=subcategory,
                                           item_id=item.id,
                                           )
        markup.insert(
            InlineKeyboardButton(text=button_text,
                                 callback_data=callback_data)
        )
    markup.row(
        InlineKeyboardButton(
            text='Назад ◀',
            callback_data=make_callback_data(
                level=CURRENT_LEVEL - 1,
                categories=category
            )
        )
    )
    markup.row(
        InlineKeyboardButton(
            text='Сильно назад ⏪',
            callback_data=make_callback_data(
                level=CURRENT_LEVEL - 2
            )
        )
    )

    return markup


async def items_keyboard(category, subcategory):
    CURRENT_LEVEL = 2
    markup = InlineKeyboardMarkup(row_width=1)
    items = await get_items(category, subcategory)
    for item in items:
        button_text = f'{item.name}'
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1,
                                           categories=category,
                                           subcategories=subcategory,
                                           item_id=item.id)
        markup.insert(InlineKeyboardMarkup(text=button_text, callback_data=callback_data))
    markup.row(InlineKeyboardButton(text='Назад',
                                    callback_data=make_callback_data(
                                        level=CURRENT_LEVEL - 1,
                                        categories=category)))
    return markup
