import os.path
import json
import datetime
from transction_obj import transaction


def load_json_from_file(path_action, file_name):
    """
    Функция возвращает объект по строкам из json файла
    """
    file_ID = os.path.join(path_action, file_name)  # Считываем файл с диска
    with open(file_ID, 'r', encoding='utf-8') as file_JS:  # Читаем файл построчно
        return json.load(file_JS)


def filter_date(text_date: str):
    """
    Функция фильтрует полученную дату и возвращает в нужной нам форме
    """
    position = text_date.find('T')
    str_date = text_date[0:position]
    str_date_dif = str_date.split('-')
    return str_date_dif[2] + "." + str_date_dif[1] + "." + str_date_dif[0]


def filter_date_2(text_date: str):
    """
    Функция фильтрует полученную дату и возвращает в нужной нам форме уже для получения точной даты для datetime.date
    """
    position = text_date.find('T')
    str_date = text_date[0:position]
    str_date_dif = str_date.split('-')
    return str_date_dif


def filter_score(text_score: str):
    """
    Функция фильтрует приводит счет в надлежащий нам вид и скрывает цифры
    """
    score = []
    for item in text_score:
        if item.isdigit():
            score.append(item)
    score_out = []
    for index, item in enumerate(score):
        score_out.append(item)
        if ((index + 1) % 4) == 0:
            score_out.append(" ")
    if len(score_out) == 20:
        for index in range(10, 14):
            score_out[index] = 'Х'
    elif len(score_out) == 25:
        for index in range(15, 19):
            score_out[index] = 'Х'
    score_text = []
    for item in text_score:
        if item.isalpha() or item == " ":
            score_text.append(item)
    return "".join(score_text) + "".join(score_out)


def sort_obj_from_date(transaction):
    """
    Функция предназначена для сортировки по дате (ключ для сортировки)
    """
    Year = filter_date_2(transaction.get_date())[0]
    Month = filter_date_2(transaction.get_date())[1]
    Day = filter_date_2(transaction.get_date())[2]
    # Возвращаем дату в формате "2018-21-03"
    date_temp = datetime.date(int(Year), int(Month), int(Day))
    # Преобразуем в число
    return date_temp.strftime("%Y%m%d")
