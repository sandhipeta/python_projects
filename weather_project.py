import requests
from pprint import pprint

API_Key = "bc37e15ff1590a081076e9ee7f1ab7ff"

city = input("Enter a city: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + API_Key + "&q=" +city

weather_data = requests.get(base_url).json()

pprint(weather_data)