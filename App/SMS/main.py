import requests

api_key = "502a71b75de849618cc4d2c6cd5480ee"

parameters = {
    "q":"Londo,UK",
    "appid":api_key
}

response = requests.get("https://api.openweathermap.org/data/2.5/weather")
data = response.json()
print(data)