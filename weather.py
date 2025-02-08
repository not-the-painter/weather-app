import json
import os

import requests  # type: ignore


def get_current_weather(city):
    KEY = os.getenv("WEATHER_API_KEY")
    BASE_URL = "https://api.weatherapi.com/v1/"
    CURRENT = "current.json"
    PARAMS = f"?key={KEY}&q={city}"
    URL = f"{BASE_URL}{CURRENT}{PARAMS}"

    response = requests.get(URL)
    if response.status_code != 200:
        return f"Status code {response.status_code}. No response"

    json_response = json.loads(response.text)
    city = json_response["location"]["name"]
    country = json_response["location"]["country"]
    temp = json_response["current"]["temp_c"]
    feels_like = json_response["current"]["feelslike_c"]
    condition = json_response["current"]["condition"]["text"]

    current_weather = f"Current conditions for {city}, {country}:\n{condition}\nTemp: {temp}C\nFeels like: {feels_like}C"
    return current_weather


if __name__ == "__main__":
    get_current_weather("Ottawa")
