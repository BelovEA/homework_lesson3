"""Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия,
 год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Осуществ
 ить вывод данных о пользователе одной строкой.
"""
def data(name, surname, year, city, email, phone_number):
    """ Данная функция используется для сбора данных от пользователя(имя, фамилия,год рождения, город проживания, email, телефон)
и осуществелие вывода этих параметров одной строкой.
 """
    print(f"Персональные данные мистера X: имя - {name}, фамилия - {surname}, город - {city}, email - {email}, номер телефона - {phone_number}")
data(name = input("введите имя: "), surname = input("введите фамилию: "), year = int(input("введите год: ")), city = input("введите город: "), email = input("введите @mail адресс: "), phone_number = int(input("введите номер телефона: ")))
