import json
import os

import requests


def get_current_weather(city):
    KEY = os.environ.get("WEATHER_API_KEY")
    BASE_URL = "https://api.weatherapi.com/v1/"
    CURRENT = "current.json"
    PARAMS = f"?key={KEY}&q={city}"
    URL = f"{BASE_URL}{CURRENT}{PARAMS}"

    response = requests.get(URL)
    json_response = json.loads(response.text)
    country = json_response["location"]["country"]
    temp = json_response["current"]["temp_c"]
    feels_like = json_response["current"]["feelslike_c"]
    condition = json_response["current"]["condition"]["text"]

    current_weather = f"Current conditions for {city}, {country}:\n{condition}\nTemp: {temp}C\nFeels like: {feels_like}C"

    return current_weather
