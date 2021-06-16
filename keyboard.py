from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, \
    ReplyKeyboardRemove
import content


# ! TODO Лишний код. Пока оставлю для примера

class Keyboard:
    button_show_all_modules = InlineKeyboardButton(text=content.SERVICE_BUTTON['show_all_modules'],
                                                   callback_data='show_all_modules')

    back_to_module_1 = InlineKeyboardButton(text='◀К модулю 1', callback_data='module_1')
    back_to_module_2 = InlineKeyboardButton(text='◀К модулю 2', callback_data='module_2')
    back_to_module_3 = InlineKeyboardButton(text='◀К модулю 3', callback_data='module_3')
    back_to_module_4 = InlineKeyboardButton(text='◀К модулю 4', callback_data='module_4')
    back_to_module_5 = InlineKeyboardButton(text='◀К модулю 5', callback_data='module_5')
    back_to_module_6 = InlineKeyboardButton(text='◀К модулю 6', callback_data='module_6')
    back_to_module_7 = InlineKeyboardButton(text='◀К модулю 7', callback_data='module_7')

    def back_to_module(self, module):
        back_to_module = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
        back_button = InlineKeyboardButton(text=f'Back button {module}', callback_data='module_1')
        # back_to_module.add(self.button_show_all_modules)
        return back_to_module

    def phone_request(self):
        phone_kb = ReplyKeyboardMarkup(resize_keyboard=True,
                                       keyboard=[
                                           [
                                               KeyboardButton(text="Проверить регистрацию на курсе 📱",
                                                              request_contact=True)
                                           ]
                                       ])
        return phone_kb

    def all_modules(self, module_dict):
        module_kb = InlineKeyboardMarkup(row_width=1)
        for exercise_key, exercise_name in module_dict.items():
            module_button = InlineKeyboardButton(text=exercise_name,
                                                 callback_data=exercise_key)
            module_kb.add(module_button)
        return module_kb

    def exercise_in_module(self, exercise_dict):
        exercise_kb = InlineKeyboardMarkup(row_width=1)

        for exercise_key, exercise_name in exercise_dict.items():
            exercise_button = InlineKeyboardButton(text=exercise_name,
                                                   callback_data=exercise_key)
            exercise_kb.add(exercise_button)
        exercise_kb.add(self.button_show_all_modules)
        return exercise_kb

    def lessons(self, lessons_dict, module):
        lessons_kb = InlineKeyboardMarkup(row_width=3)
        lesson_number = 0
        for lesson_key, value in lessons_dict.items():
            lesson_number += 1
            lesson_button = InlineKeyboardButton(text=f'{value["name"]}',
                                                 callback_data=lesson_key)

            lessons_kb.add(lesson_button)
        back_to = InlineKeyboardButton(text=f'◀Вернуться к модулю {module}', callback_data=f'module_{module}')
        lessons_kb.add(back_to)
        lessons_kb.add(self.button_show_all_modules)
        return lessons_kb
