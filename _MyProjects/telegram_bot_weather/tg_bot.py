import requests
from datetime import date
from datetime import datetime
from config import tg_bot, open_weather
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_bot)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Сводка какого города интересует?")

@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather}")
        data = r.json()

        day = date.today().strftime('%d-%m-%Y')
        cur_weather = round(float(data['main']['temp'])-273.15, 0)
        humidity = data['main']['humidity']
        wind = data['wind']['speed']
        pressure = round((float(data['main']['pressure'])*0.750062), 2)
        time_sunrise = datetime.fromtimestamp(data['sys']['sunrise']).time()
        time_sunset = datetime.fromtimestamp(data['sys']['sunset']).time()
        await message.reply(f"{day} в {message.text}:\nТемпература: {cur_weather}C\u00B0\nВлажность: {humidity}%\n"
              f"Скорость ветра: {wind} м/с\nАтмосферное давление: {pressure} мм.рт.ст.\n"
              f"Восход в {time_sunrise}\n"
              f"Закат в {time_sunset}")
    except:
        await message.reply('Проверьте название города')

if __name__ == '__main__':
    executor.start_polling(dp)