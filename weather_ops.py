import asyncio
import json
import python_weather as pw

async def get_weather(location:str) -> str:
    async with pw.Client(unit=pw.METRIC) as client:
        weather = await client.get(location)
        unit = '\u00b0C' if weather.unit == pw.METRIC else '\u00b0F'
        weather_data = {
            'location': location,
            'temperature': weather.temperature,
            'unit': unit,
            'humidity': weather.humidity
        }
        return json.dumps(weather_data)

if __name__ == '__main__':
    weather_data_json = asyncio.run(get_weather('Łomianki'))
    print('IN JSON: ', weather_data_json, sep='\t')
    weather_data_dictionary = json.loads(weather_data_json) # this parses JSON string to a Dictionary
    print('IN MAP: ',
          weather_data_dictionary['location'],
          weather_data_dictionary['temperature'],
          weather_data_dictionary['unit'],
          weather_data_dictionary['humidity'],
          sep='\t')