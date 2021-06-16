# Клавиатура с меню-навигацией по курсу

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

menu_cd = CallbackData('show_menu', 'level', 'category', 'subcategory', 'item_id')


def make_callback_data(level, category=0, subcategory=0, item_id=0):
    '''
    С помощью этой функции будем формировать коллбек дату для каждого элемента меню, в зависимости от
    переданных параметров. Если Подкатегория, или айди товара не выбраны - они по умолчанию равны нулю
    '''
    return menu_cd.new(level=level, category=category, subcategory=subcategory, item_id=item_id)

async def categories_keyboard():
    pass

async def subcategories_keyboard():
    pass
async def items_keyboard():
    pass
