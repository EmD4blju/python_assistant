import json
import requests
import dotenv as env

config = env.dotenv_values("credentials/.env")


def get_weather(location: str) -> str:  # [Notice]: function gets current weather in the given location
    url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={config.get("W_API_KEY")}&units=metric'
    weather_json = requests.get(url)
    weather_dict = json.loads(weather_json.text)
    return get_weather_info(weather_dict)


def get_weather_info(weather_dict: dict) -> str:
    weather_info = weather_dict['main']
    return f"""
Temperatura: {weather_info['temp']} \u00b0Celsjusza,
Ciśnienie: {weather_info['pressure']} hPa,
Wilgotność: {weather_info['humidity']}
"""


if __name__ == '__main__':
    print(get_weather('Warszawa'))
