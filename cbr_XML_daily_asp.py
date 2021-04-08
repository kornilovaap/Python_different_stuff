"""
Разработать программу, которая выводит курс японских иен к российскому рублю, на
основании данных, запрошенных с сайта http://www.cbr.ru/scripts/XML_daily.asp
"""
from xml.dom import minidom
from urllib.request import urlopen

# Открываем для парсинга файл
url = 'http://www.cbr.ru/scripts/XML_daily.asp'
dom = minidom.parse(urlopen(url))
# извлекаем дату
root = dom.getElementsByTagName("ValCurs")[0]
date = root.getAttribute('Date')
# собираем все валюты
currency = dom.getElementsByTagName("Valute")
# по id валюты извлекаем нужные данные
for val in currency:
    if val.getAttribute("ID") == 'R01820':
        value = val.getElementsByTagName("Value")[0]
        nominal = val.getElementsByTagName("Nominal")[0]
        jpy = nominal.firstChild.data
        jpy = round(float(jpy.replace(',', '.')), 2)
        rub = value.firstChild.data
        # заменяем , на . чтобы превратить str -> float и оркглить до 2ух зхнаков
        rub = round(float(rub.replace(',', '.')), 2)

        print(
            f"курс японских йен к российскому рублю на {date}:"
            f"\n>>> {jpy} JPY к {rub} RUB, или"
            f"\n>>> {round(jpy / 100, 2)} JPY к {round(rub / 100, 2)} RUB.")

# курс японских йен к российскому рублю на 09.04.2021:
# >>> 100.0 JPY к 70.43 RUB, или
# >>> 1.0 JPY к 0.7 RUB.
    
