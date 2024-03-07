"""
7. (МОДУЛЬ 4) В проекте создать новый модуль victory.py. Задание
Написать или улучшить программу Викторина из предыдущего дз
(Для тренировки предлагаю не пользоваться никакими библиотеками кроме random)
Есть 10 известных людей и их даты рождения в формате '02.01.1988' ('dd.mm.yyyy')
- предлагаю для тренировки пока использовать строку
Программа выбирает из этих 10-и 5 случайных людей,
это можно реализовать с помощью модуля random и функции sample
Пример использования sample:
import random
numbers = [1, 2, 3, 4, 5]

# 2 - количество случайных элементов
result = random.sample(numbers, 2)

print(result) # [5, 1]

После того как выбраны 5 случайных людей, предлагаем пользователю ввести их дату рождения
пользователь вводит дату в формате 'dd.mm.yyyy'

Например, 03.01.2009, если пользователь ответил неверно, то выводим правильный ответ, но уже в следующем виде:
третье января 2009 года, склонением можно пренебречь

В конце считаем количество правильных и неправильных ответов и предлагаем начать снова
"""

import random

FAMOUS_PEOPLES = [
    ["Лев Толстой", "09.09.1828"],
    ["Петр Чайковский", "07.05.1840"],
    ["Федор Достоевский", "11.11.1821"],
    ["Антон Чехов", "29.01.1860"],
    ["Василий Кандинский", "16.12.1866"],
    ["Сергей Эйзенштейн", "22.01.1898"],
    ["Марина Цветаева", "08.10.1892"],
    ["Анна Ахматова", "23.06.1889"],
    ["Дмитрий Шостакович", "25.09.1906"],
    ["Андрей Сахаров", "21.05.1921"]
]


def confirmation(message='Выполнить действие? (да/нет): '):
    answer = ''
    while answer not in ('да', 'нет', 'lf', 'ytn'):
        answer = input(message).lower()

    if answer == 'lf':
        print('Получен ответ "да"')
    if answer == 'ytn':
        print('Получен ответ "нет"')

    return answer in ('да', 'lf')


def get_date_str(date):
    day, month, year = date.split('.')
    months = {
        "01": "января",
        "02": "февраля",
        "03": "марта",
        "04": "апреля",
        "05": "мая",
        "06": "июня",
        "07": "июля",
        "08": "августа",
        "09": "сентября",
        "10": "октября",
        "11": "ноября",
        "12": "декабря"
    }
    days = {
        "01": "первое", "02": "второе", "03": "третье", "04": "четвертое", "05": "пятое",
        "06": "шестое", "07": "седьмое", "08": "восьмое", "09": "девятое", "10": "десятое",
        "11": "одиннадцатое", "12": "двенадцатое", "13": "тринадцатое", "14": "четырнадцатое",
        "15": "пятнадцатое", "16": "шестнадцатое", "17": "семнадцатое", "18": "восемнадцатое",
        "19": "девятнадцатое", "20": "двадцатое", "21": "двадцать первое", "22": "двадцать второе",
        "23": "двадцать третье", "24": "двадцать четвертое", "25": "двадцать пятое",
        "26": "двадцать шестое", "27": "двадцать седьмое", "28": "двадцать восьмое",
        "29": "двадцать девятое", "30": "тридцатое", "31": "тридцать первое"
    }

    day_text = days.get(day, day)
    month_text = months.get(month, month)
    year_text = year

    return f"{day_text} {month_text} {year_text}"


def get_statistic(questions_count, correct_answers):
    incorrect_answers = questions_count - correct_answers
    correct_percent = 100 * correct_answers / questions_count
    incorrect_percent = 100 * incorrect_answers / questions_count
    return incorrect_answers, correct_percent, incorrect_percent


def play_victory():
    questions_count = 5
    five_famous_peoples = random.sample(FAMOUS_PEOPLES, questions_count)

    continue_game = True
    while continue_game:
        correct_answers = 0

        for famous_people in five_famous_peoples:
            birth_date = input(f"Укажите дату рождения человека с именем {famous_people[0]} в формате dd.mm.yyyy: ")
            if birth_date == famous_people[1]:
                print('Вы правильно указали дату рождения!')
                correct_answers += 1
            else:
                date_str = get_date_str(famous_people[1])
                print(f"Правильный ответ: {date_str} года")

        incorrect_answers, correct_percent, incorrect_percent = get_statistic(questions_count, correct_answers)

        print(f'Правильных ответов: {correct_answers}')
        print(f'Неправильных ответов: {incorrect_answers}')
        print(f'Процент правильных ответов: {correct_percent}%')
        print(f'Процент неправильных ответов: {incorrect_percent}%')

        continue_game = confirmation('Хотите ли вы продолжить игру? (да/нет): ')

