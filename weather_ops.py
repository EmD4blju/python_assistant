import asyncio
import json
import python_weather as pw

async def get_weather(location:str) -> str: # [Notice]: function gets current weather in the given location
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