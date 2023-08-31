import requests
from id import api_key

def city():
    url = "https://api.openweathermap.org/geo/1.0/direct"
    params = {
        "q": "Lyon",
        "appid": api_key
    }

    response = requests.get(url, params=params)
    data = response.json()
    return data

cities = city()[0]


def weather():

    url_weather = "https://api.openweathermap.org/data/2.5/weather"

    params_weather = {
        "lat": cities.get("lat"),  # Utiliser les coordonnées de la ville
        "lon": cities.get("lon"),
        "appid": api_key
    }

    response_weather = requests.get(url_weather, params=params_weather)
    data_weather = response_weather.json()

    return data_weather
