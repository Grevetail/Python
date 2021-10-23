import requests
from datetime import date
from datetime import datetime
from pprint import pprint
from config import open_weather

def get_weather(city, open_weather):
    try:
        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather}")
        data = r.json()

        day = date.today().strftime('%d-%m-%Y')
        cur_weather = round(float(data['main']['temp'])-273.15, 0)
        humidity = data['main']['humidity']
        wind = data['wind']['speed']
        pressure = round((float(data['main']['pressure'])*0.750062), 2)
        time_sunrise = datetime.fromtimestamp(data['sys']['sunrise']).time()
        time_sunset = datetime.fromtimestamp(data['sys']['sunset']).time()
        print(f"{day} в {city}:\nТемпература: {cur_weather}C\u00B0\nВлажность: {humidity}%\n"
              f"Скорость ветра: {wind} м/с\nАтмосферное давление: {pressure} мм.рт.ст.\n"
              f"Восход в {time_sunrise}\n"
              f"Закат в {time_sunset}")
    except Exception as ex:
        print(ex)
        print('Проверьте название города')

def main():
    city = input('Введите город: ') or 'Saint Petersburg'
    get_weather(city, open_weather)

if __name__ == '__main__':
    main()