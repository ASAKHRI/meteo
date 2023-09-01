import requests
from id import api_key
import pandas as pd

def city(CITY):
    url = "https://api.openweathermap.org/geo/1.0/direct"
    params = {
        "q": CITY,
        "appid": api_key
    }

    response = requests.get(url, params=params)
    data = response.json()
    return data




def weather(CITY, unit):
    
    url_weather = "https://api.openweathermap.org/data/2.5/weather"
    unit
    params_weather = {
        "lat": city(CITY)[0].get("lat"),  # Utiliser les coordonnées de la ville
        "lon": city(CITY)[0].get("lon"),
        "appid": api_key,
        "units" : unit
    }

    response_weather = requests.get(url_weather, params=params_weather)
    weather_data = response_weather.json()
    description = weather_data["weather"][0]["description"]
    temp = int(round(weather_data["main"]["temp"],0))
    temp_feels_like = int(round(weather_data["main"]["feels_like"],0))
    temp_min = int(round(weather_data["main"]["temp_min"],0))
    temp_max = int(round(weather_data["main"]["temp_max"],0))
    humidity = weather_data["main"]["humidity"]
    icon = weather_data["weather"][0]["icon"]
    

        # Create a dataframe
    df = pd.DataFrame({
        "Description": [description],
        "Temperature": [temp],
        "Feels Like": [temp_feels_like],
        "Min Temperature": [temp_min],
        "Max Temperature": [temp_max],
        "Humidity": [humidity],
        "icon" : [icon]
    })
    print(df)
    return df
    