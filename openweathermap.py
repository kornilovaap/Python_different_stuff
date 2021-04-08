"""
Разработать программу, которая будет отправлять запрос к сервису прогноза погоды   
https://openweathermap.org/ с использованием бесплатного плана (Free, требует регистрации на сайте)     
и на основании полученных данных выводить следующую информацию:   
- Максимальное давление за предстоящие 5 дней (включая текущий);   
Выводить данные для Вашего города (указав либо долготу/широту, либо идентификатор города из документации сайта).    
"""
import requests  # Модуль для обработки URL

api_key = "afac3a20be40ee9757f6c5bae89ba96f"

# 1. Находим id нужного города
try:
    # запросили у пользователя город
    city = input("Введите город >>> ").title()
    # получаем json данные
    json_id = requests.get("http://api.openweathermap.org/data/2.5/find", params={'q': city, 'APPID': api_key}).json()
    # выбираем оттуда все города и их страны
    cities = [f"{d['name']},{d['sys']['country']}" for d in json_id['list']]
    print(f"Найдено: {cities}")
    # Может быть несколько городов, например ['Moscow,RU', 'Moscow,US', 'Moscow,US', 'Moscow,RU']

    # поэтому деаем проверку, если городов в мире больше одного
    a = 0
    if len(cities) > 1:
        a = int(input("Введите порядковый номер вашего города в списке (1, 2, и т.д.) >>> "))
    # находим айди по городу и стране
    city_id = json_id['list'][a - 1]['id']
    print('city_id=', city_id)
except Exception as e:
    print("Ошибка ввода, или город не найден", e)
    pass

# 2. Находим давление
try:
    # получаем json данные с погодой
    json_data = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                             params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': api_key}).json()
    # сюда запишем все измерения давления за 5 дней
    pressures = []
    # собираем все показатели давления за 5 суток
    for i in json_data['list']:
        pressure = i['main']['pressure']
        pressures.append(pressure)
    # выводим максимальное значение
    print(f"max_pressure = {max(pressures)}")
except Exception as e:
    print("Ошибка, значения не найдены", e)
    pass

# Введите город >>> москва
# Найдено: ['Moscow,RU', 'Moscow,US', 'Moscow,US', 'Moscow,RU']
# Введите порядковый номер вашего города в списке (1, 2, и т.д.) >>> 1
# city_id= 524901
# max_pressure = 1032

# Введите город >>> чебоксары
# Найдено: ['Cheboksary,RU']
# city_id= 569696
# max_pressure = 1034
    
