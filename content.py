# TODO Полностью переделать, убрать все ссылки в базу данных, в данном файле оставить только текст сообщений


start_messages = 'Привет ☺' \
                 '\n\nДобро пожаловать на марафон «Геометрия для ОГЭ с нуля до профи»' \
                 '\n\nСначала пройди регистрацию, нажав кнопку 👇🏻'
registration_ok = 'Окей, ты зарегистрирован.'
registration_error = 'Что-то пошло не так. Напиши @nfd_admin'


def reg_ok(tariff):
    tariff_name = ''
    if tariff[0] == 'basic':
        tariff_name = 'Я сам'
    elif tariff[0] == 'normal':
        tariff_name = 'Я с поддержкой'
    elif tariff[0] == 'advanced':
        tariff_name = 'Я с Настей'
    text = 'Супер! Теперь ты зарегистрирован 😉\n\n' \
           f'Твой тариф: "{tariff_name}"\n\nЖелаю удачи!'
    return text


MESSAGES = {
    'start': start_messages,
    'reg_ok': registration_ok,
    'reg_not_ok': registration_error,
    'module_selection': 'Выбери день и тему 👇🏻'
}

SERVICE_BUTTON = {
    'phone_request': 'Проверить регистрацию на курсе 📱',
    'show_all_modules': '⏪ Вернуться к списку модулей'
}

MODULE_NAME = {
    'module_1': 'День 1 Треугольники, углы и расстояния Ч1',
    'module_2': 'День 2 Треугольники, углы и расстояния Ч2',
    'module_3': 'День 3 Четырехугольники и многоугольники',
    'module_4': 'День 4 Круг и окружность',
    'module_5': 'День 6 Задание №23 ОГЭ (Геометрическая задача на вычисление)',
    # 'module_6': 'День 6 Вторая часть (задания 23 и 24)',
    # 'module_7': 'День 7 Вторая часть (задания 23 и 24)'
}

EXERCISE_NAME = {'exercise_15': '№15 ОГЭ – Нахождение геометрических величин',
                 'exercise_16': '№16 ОГЭ – Окружность, круг и их элементы',
                 'exercise_17': '№17 ОГЭ – Площади ',
                 'exercise_18': '№18 ОГЭ – Фигуры на квадратной решетке',
                 'exercise_19': '№19 ОГЭ – Анализ геометрических высказываний про треугольники',
                 'exercise_23': '№23 ОГЭ - Геометрическая задача на вычисление',
                 'exercise_24': '№24 ОГЭ - Геометрическая задача на доказательство',
                 'exercise_rp': 'Параллелограммы и Ромбы',
                 'exercise_ps': 'Прямоугольники и Квадраты',
                 'exercise_tr': 'Трапеции',
                 'exercise_mg': 'Многоугольники',
                 'exercise_ug': 'Вписанные и центральные углы',
                 'exercise_el': 'Элементы окружности',
                 'exercise_rs': 'Площадь круга, площадь сектора, длина окружности, длина дуги',
                 'exercise_ro': 'Вписанные и описанные окружности',
                 'exercise_ok': 'Окружности',
                 'exercise_p1': 'Четырехугольники',
                 'exercise_t1': 'Треугольники'

                 }

module = {
    'module_1': {'m1_exercise_15': EXERCISE_NAME['exercise_15']},
    'module_2': {'m2_exercise_17': EXERCISE_NAME['exercise_17'],
                 'm2_exercise_18': EXERCISE_NAME['exercise_18'],
                 'm2_exercise_19': EXERCISE_NAME['exercise_19']
                 },
    'module_3': {'m3_exercise_rp': EXERCISE_NAME['exercise_rp'],
                 'm3_exercise_ps': EXERCISE_NAME['exercise_ps'],
                 'm3_exercise_tr': EXERCISE_NAME['exercise_tr'],
                 'm3_exercise_mg': EXERCISE_NAME['exercise_mg'],
                 'm3_exercise_19': EXERCISE_NAME['exercise_19']
                 },
    'module_4': {'m4_exercise_ug': EXERCISE_NAME['exercise_ug'],
                 'm4_exercise_el': EXERCISE_NAME['exercise_el'],
                 'm4_exercise_rs': EXERCISE_NAME['exercise_rs'],
                 'm4_exercise_ro': EXERCISE_NAME['exercise_ro'],
                 'm4_exercise_19': EXERCISE_NAME['exercise_19']
                 },
    'module_5': {'m5_exercise_23': EXERCISE_NAME['exercise_23'],
                 },
    # 'module_6': {,m6
    #          'm6_exercise_ok': EXERCISE_NAME['exercise_ok']},
    # 'module_7': {'m7_exercise_24': EXERCISE_NAME['exercise_24']}

}

exercise = {'m1_exercise_15':
                {'m1_exc15_l1': {'name': 'Урок 1 Углы',
                                 'link': 'https://youtu.be/kb_FkSGssmo',
                                 'practice': 'https://youtu.be/NT8F0LicoIY',
                                 'homework': 'https://forms.gle/yjRS5a7Kza9PeUFh9',
                                 'check_list': 'https://drive.google.com/file/d/1bhAgCZ_npJ7tvclyvHIFIyAfCHvdktMA/view?usp=sharing',
                                 'workbook': 'https://drive.google.com/file/d/1Y3jwPQRX2hKv8O4qmu0VRWEAEpHxhI2D/view?usp=sharing',
                                 'cheatsheet': 'https://drive.google.com/file/d/1tCCoQfY7cGbQC0Ti9XuUJy2um0g4zN_S/view?usp=sharing'},
                 'm1_exc15_l2': {'name': 'Урок 2 Треугольники общего вида',
                                 'link': 'https://youtu.be/Xyf_7kst53A',
                                 'practice': 'https://youtu.be/3snWwsX_vrs',
                                 'homework': 'https://forms.gle/bxTs16KTaZjZWBDV7',
                                 'check_list': 'https://drive.google.com/file/d/1IGi1RymLVnyRSWeZz0YdyX7RTB_vftCo/view?usp=sharing',
                                 'workbook': 'https://drive.google.com/file/d/1NObf7uSw0sdCOif1YTJF9E74-siiuw0J/view?usp=sharing',
                                 'cheatsheet': 'https://drive.google.com/file/d/1tCCoQfY7cGbQC0Ti9XuUJy2um0g4zN_S/view?usp=sharing'
                                 },
                 'm1_exc15_l3': {'name': 'Урок 3 Прямоугольные треугольники',
                                 'link': 'https://youtu.be/etMdewvScXs',
                                 'practice': 'https://youtu.be/0Xl9cFRowk8',
                                 'homework': 'https://forms.gle/HbVeYL2fRGZjzjgd9',
                                 'check_list': 'https://drive.google.com/file/d/1NVNreJE60Ki7FiPVazTcYY_dR1fhpnA0/view?usp=sharing',
                                 'workbook': 'https://drive.google.com/file/d/1f9Gys5VFD4UkclR1k99q-M4LHR5QtU9b/view?usp=sharing',
                                 'cheatsheet': 'https://drive.google.com/file/d/1tCCoQfY7cGbQC0Ti9XuUJy2um0g4zN_S/view?usp=sharing'
                                 },
                 'm1_exc15_l4': {'name': 'Урок 4 Равнобедренные треугольники',
                                 'link': 'https://youtu.be/WcGCXP_vThY',
                                 'practice': 'https://youtu.be/yq-SMLrHYbg',
                                 'homework': 'https://forms.gle/s9xZQ39ef3er1tpv9',
                                 'check_list': 'https://drive.google.com/file/d/1XOCj_lk3MVYCY-2-ciZ8y4V9-1fD7jof/view?usp=sharing',
                                 'workbook': 'https://drive.google.com/file/d/1nWEHXYTSJpmfzc4FmluWccQl3Pdg77Nv/view?usp=sharing',
                                 'cheatsheet': 'https://drive.google.com/file/d/1tCCoQfY7cGbQC0Ti9XuUJy2um0g4zN_S/view?usp=sharing'
                                 }, },
            # Пятый день, ВТОРАЯ ЧАСТЬ
            'm5_exercise_23': {
                'm5_exc23_l1': {'name': '1. Треугольники',
                                'link': 'Отсутствует',
                                'practice': '1. https://youtu.be/ve8-ZbtMmMc\n'
                                            '2. https://youtu.be/2674TncPBFU',
                                'homework': 'https://drive.google.com/file/d/1SlCyWy9z2Pvu5_4MT73Z3ZDTD5-t99Zd/view?usp=sharing'
                                            '\n\nОтветы: https://docs.google.com/spreadsheets/d/1Z_1caa0h5_ZcB5Ags1URMO7bO1SFCUyFjJ-eetnbG5E/edit?usp=sharing',
                                'check_list': 'https://drive.google.com/file/d/1KM0hS16xiC2estMyjRVpyBxXolSZFTPX/view?usp=sharing',
                                'workbook': 'https://drive.google.com/file/d/1SlCyWy9z2Pvu5_4MT73Z3ZDTD5-t99Zd/view?usp=sharing'
                                            '\n\nОтветы: https://docs.google.com/spreadsheets/d/1Z_1caa0h5_ZcB5Ags1URMO7bO1SFCUyFjJ-eetnbG5E/edit?usp=sharing',
                                'cheatsheet': 'https://drive.google.com/file/d/1tCCoQfY7cGbQC0Ti9XuUJy2um0g4zN_S/view?usp=sharing'},
                'm5_exc23_l2': {'name': '2. Четырехугольники',
                                'link': 'Отсутствует',
                                'practice': '1. https://youtu.be/P9ZuYuRwcTY\n'
                                            '2. https://youtu.be/H0TsI2f7AzU',
                                'homework': 'https://drive.google.com/file/d/1Q952gOmw8h04Sz7yUkhdZIG1WdDZCjWN/view?usp=sharing'
                                            '\n\nОтветы: https://docs.google.com/spreadsheets/d/16IQlJsHAE9upth7FckHTjZ3uLdV5ENaRyRNQzjY4TXI/edit?usp=sharing',
                                'check_list': 'https://drive.google.com/file/d/13eJWy_ZeFXH47_vsK7rS8MUQ1LwdwgXM/view?usp=sharing',
                                'workbook': 'https://drive.google.com/file/d/1Q952gOmw8h04Sz7yUkhdZIG1WdDZCjWN/view?usp=sharing'
                                            '\n\nОтветы: https://docs.google.com/spreadsheets/d/16IQlJsHAE9upth7FckHTjZ3uLdV5ENaRyRNQzjY4TXI/edit?usp=sharing',
                                'cheatsheet': 'https://drive.google.com/file/d/1cJKrtG2UPqLEJRbVGAQTQTVWe2x9RSTK/view?usp=sharing'},
            },

            # ТРЕУГОЛЬНИКИ ВТОРОЙ ДЕНЬ
            'm2_exercise_17': {
                'm2_exc17_l1': {'name': 'Урок 1 Площади',
                                'link': 'https://youtu.be/FyyGvaVwu6E',
                                'practice': 'https://youtu.be/n7w1LOOUIWU',
                                'homework': 'https://forms.gle/3hkHGxU1gkLtae3z9',
                                'check_list': 'https://drive.google.com/file/d/1p_zCXdbkn-UULNtsWACu7lyDsx2rJy6L/view?usp=sharing',
                                'workbook': 'https://drive.google.com/file/d/10V-6ZlJcAUKVvZlLyOXYyQ5bGGd5_cWN/view?usp=sharing',
                                'cheatsheet': 'https://drive.google.com/file/d/1tCCoQfY7cGbQC0Ti9XuUJy2um0g4zN_S/view?usp=sharing'}, },
            'm2_exercise_18': {
                'm2_exc18_l1': {'name': 'Урок 1 Квадратная решетка',
                                'link': 'Отстутствует',
                                'practice': 'https://youtu.be/f_h59Z4EHZs',
                                'homework': 'https://forms.gle/szNaaTs7f2e41GFe6',
                                'check_list': 'https://drive.google.com/file/d/1bfenJGL3jeY7d5xfjFz8IZH9sS0FH_yI/view?usp=sharing',
                                'workbook': 'https://drive.google.com/file/d/1nKnaC6Nfwl8S2jaaUXdnCi2T5iyhunfs/view?usp=sharing',
                                'cheatsheet': 'https://drive.google.com/file/d/1tCCoQfY7cGbQC0Ti9XuUJy2um0g4zN_S/view?usp=sharing'}, },
            'm2_exercise_19': {
                'm2_exc19_l1': {'name': 'Урок 1 Анализ высказываний',
                                'link': 'https://youtu.be/WjSmAU8cWWc',
                                'practice': 'Отстутствует',
                                'homework': 'https://forms.gle/CtuZmFBoL2WYj4ow8',
                                'check_list': 'https://drive.google.com/file/d/1QykE-QyP-NiBN3nTLvImM-fdBfsmj4K5/view?usp=sharing',
                                'workbook': 'Отсутствует',
                                'cheatsheet': 'https://drive.google.com/file/d/1tCCoQfY7cGbQC0Ti9XuUJy2um0g4zN_S/view?usp=sharing'}, },
            # Третий день
            'm3_exercise_rp': {'m3_excrp_l1':
                                   {'name': 'Задания №15, №17, №18 ОГЭ',
                                    'link': 'https://youtu.be/0FgAnUiKUIw',
                                    'practice': '\n Задание №15: https://youtu.be/V8KiRFGWJRU \n\n'
                                                'Задание №17: https://youtu.be/kPcncU2W9hs \n\n'
                                                'Задание №18: https://youtu.be/W4d4dVk18v4',
                                    'homework': 'https://forms.gle/if9DGQRKBY4PQ5Kd6',
                                    'check_list': 'https://drive.google.com/file/d/1HwVr5BIXhnleQPexCTpfV1gHlNpNZquJ/view?usp=sharing',
                                    'workbook': 'https://drive.google.com/file/d/1c7nqI4-v0CQeUWZjpYNdhhxdZM21eeuu/view?usp=sharing',
                                    'cheatsheet': 'https://drive.google.com/file/d/1cJKrtG2UPqLEJRbVGAQTQTVWe2x9RSTK/view?usp=sharing'}, },
            'm3_exercise_ps': {'m3_excps_l1':
                                   {'name': 'Задание №17 ОГЭ',
                                    'link': 'https://youtu.be/vKXQAPur3Ro',
                                    'practice': 'Задание №17: https://youtu.be/djW51hU24sY',
                                    'homework': 'https://forms.gle/C2UCjWz9GHuGWdqq7',
                                    'check_list': 'https://drive.google.com/file/d/18ZM_fKmo1t13X5lMzOAkqhTH-xv6FyCy/view?usp=sharing',
                                    'workbook': 'https://drive.google.com/file/d/1ht50vABITkyiYCqFN31gl9dcty6q5t3m/view?usp=sharing',
                                    'cheatsheet': 'https://drive.google.com/file/d/1cJKrtG2UPqLEJRbVGAQTQTVWe2x9RSTK/view?usp=sharing'}, },
            'm3_exercise_tr': {'m3_exctr_l1':
                                   {'name': 'Задания №15, №17, №18 ОГЭ',
                                    'link': 'https://youtu.be/NZJKMI_9lRA',
                                    'practice': '\n Задание №15: https://youtu.be/6qZwJ5bt-Gk \n\n'
                                                'Задание №17: https://youtu.be/kPcncU2W9hs \n\n'
                                                'Задание №18: https://youtu.be/Vy0cz0vHnGo',
                                    'homework': 'https://forms.gle/v8wBeGjqYjTS3zM69',
                                    'check_list': 'https://drive.google.com/file/d/1jw6oooIa4KnxhdDRostPEWjGKDQadRhz/view?usp=sharing',
                                    'workbook': 'https://drive.google.com/file/d/17jE2OsM0nlXuuO8t0t2HU3w9taDgJxPQ/view?usp=sharing',
                                    'cheatsheet': 'https://drive.google.com/file/d/1cJKrtG2UPqLEJRbVGAQTQTVWe2x9RSTK/view?usp=sharing'}, },
            'm3_exercise_mg': {'m3_excmg_l1':
                                   {'name': 'Задания №15 и №18 ОГЭ',
                                    'link': 'https://youtu.be/J_LNI3Kwq64',
                                    'practice': 'Задание №15 и №18: https://youtu.be/npyqAl5VwlA',
                                    'homework': 'https://forms.gle/37JejVWChaZu6hst8',
                                    'check_list': 'https://drive.google.com/file/d/1jw6oooIa4KnxhdDRostPEWjGKDQadRhz/view?usp=sharing',
                                    'workbook': 'https://drive.google.com/file/d/17jE2OsM0nlXuuO8t0t2HU3w9taDgJxPQ/view?usp=sharing',
                                    'cheatsheet': 'https://drive.google.com/file/d/1cJKrtG2UPqLEJRbVGAQTQTVWe2x9RSTK/view?usp=sharing'}, },
            'm3_exercise_19': {'m3_exc19_l1':
                                   {'name': 'Геометрические высказывания №19 ОГЭ',
                                    'link': 'Чек-лист по 19 заданию: https://drive.google.com/file/d/1xMiceoDV5b9mGDzsuHltJiJ5BtGF6Ylq/view?usp=sharing',
                                    'practice': 'Отсутствует',
                                    'homework': 'https://forms.gle/V8yMxFMpgQ8WCP4C8',
                                    'check_list': 'https://drive.google.com/file/d/1xMiceoDV5b9mGDzsuHltJiJ5BtGF6Ylq/view?usp=sharing',
                                    'workbook': 'Отсутствует',
                                    'cheatsheet': 'https://drive.google.com/file/d/1cJKrtG2UPqLEJRbVGAQTQTVWe2x9RSTK/view?usp=sharing'}, },
            # Четвертый день: окружности
            'm4_exercise_ug': {'m4_excug_l1':
                                   {'name': 'Задание №16 ОГЭ',
                                    'link': 'https://youtu.be/JYdyXVaQ_H4',
                                    'practice': 'https://youtu.be/8TFYGxeoFGo',
                                    'homework': 'https://forms.gle/y7dPuBYFaeGFxLPU6',
                                    'check_list': 'https://drive.google.com/file/d/1H0PwY8pBrUvTabvuCuyvNDUSlgADPo2U/view?usp=sharing',
                                    'workbook': 'https://drive.google.com/file/d/1jSEjYwP3l6SNw3-m2C4XnseN9wl6j4c2/view?usp=sharing',
                                    'cheatsheet': 'https://drive.google.com/file/d/1hmedhXTR_KCQE1zIff8VgMVGOS_ckLKM/view?usp=sharing'}},
            'm4_exercise_el': {'m4_excel_l1':
                                   {'name': 'Задание №16 ОГЭ',
                                    'link': 'https://youtu.be/VOtCDmkqQu4',
                                    'practice': 'https://youtu.be/l5c5X07XJ1I',
                                    'homework': 'https://forms.gle/Ba33LoDtTurxi4e88',
                                    'check_list': 'https://drive.google.com/file/d/1HeQey8sIjg92q9wv65h1NI_kbYWz9YZq/view?usp=sharing',
                                    'workbook': 'https://drive.google.com/file/d/13xD4MDr0C0GK6qAlfSDz0qMMpi1-xG4f/view?usp=sharing',
                                    'cheatsheet': 'https://drive.google.com/file/d/1hmedhXTR_KCQE1zIff8VgMVGOS_ckLKM/view?usp=sharing'}},
            'm4_exercise_rs': {'m4_excrs_l1':
                                   {'name': 'Задание №16 ОГЭ',
                                    'link': 'https://youtu.be/IUY9s_OzRo0',
                                    'practice': 'https://youtu.be/hEDaLcShAl8',
                                    'homework': 'https://forms.gle/H2Kgv7ER75T8ymet7',
                                    'check_list': 'https://drive.google.com/file/d/1og5puvswPjRb0qQPx3N9EcV-Y05Qu7IM/view?usp=sharing',
                                    'workbook': 'https://drive.google.com/file/d/1cfTXSdY-_KerxO2JlQ8b1hn2FcaeBDYm/view?usp=sharing',
                                    'cheatsheet': 'https://drive.google.com/file/d/1hmedhXTR_KCQE1zIff8VgMVGOS_ckLKM/view?usp=sharing'}},
            'm4_exercise_ro': {'m4_excro_l1':
                                   {'name': 'Задание №15 ОГЭ',
                                    'link': 'https://youtu.be/_ESK1u7hvZE',
                                    'practice': '\nЧасть 1: https://youtu.be/4Rvz9TuChTQ'
                                                '\n'
                                                'Часть 2: https://youtu.be/V7A7O6WSxKw',
                                    'homework': 'https://forms.gle/qdGnLJgR4nbD99AB6',
                                    'check_list': 'https://drive.google.com/file/d/122IjQI6iqPZJlWVgvuk0yyNs42Fe6mTG/view?usp=sharing',
                                    'workbook': 'https://drive.google.com/file/d/1L3ycy2Y5z6-8rI20buWVa5lynyICW1Lx/view?usp=sharing',
                                    'cheatsheet': 'https://drive.google.com/file/d/1hmedhXTR_KCQE1zIff8VgMVGOS_ckLKM/view?usp=sharing'}},
            'm4_exercise_19': {'m4_exc19_l1':
                                   {'name': 'Задание №19 ОГЭ',
                                    'link': 'https://youtu.be/jw09rbwPouI',
                                    'practice': ' -- \n\nЧек-лист с высказываниями: \n '
                                                'https://drive.google.com/file/d/1RByuz2PmqpTwhtWIlh7qeXIbkdsu4PqR/view?usp=sharing',
                                    'homework': 'https://forms.gle/Ls2p1nYn9p4XroC4A',
                                    'check_list': '-',
                                    'workbook': 'Отсутствует',
                                    'cheatsheet': 'https://drive.google.com/file/d/1hmedhXTR_KCQE1zIff8VgMVGOS_ckLKM/view?usp=sharing'}}

            }

module_selection = 'Выбери день'
exercise_selection = ''

lesson_selection = ''
