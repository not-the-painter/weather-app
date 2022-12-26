import json
import os
import webbrowser

import requests

city = input("Enter the city: ")
KEY = os.environ.get("WEATHER_API_KEY")
BASE_URL = "https://api.weatherapi.com/v1/"
CURRENT = "current.json"
PARAMS = f"?key={KEY}&q={city}"

URL = f"{BASE_URL}{CURRENT}{PARAMS}"

response = requests.get(URL)
# print(URL)
json_response = json.loads(response.text)
temp = json_response["current"]["temp_c"]
feels_like = json_response["current"]["feelslike_c"]
condition = json_response["current"]["condition"]["text"]


print(f"Current conditions for {city}, {json_response['location']['country']}:")
print(condition)
print(f"Temp: {temp}C")
print(f"Feels like: {feels_like}C")


# print(json_response)
