import requests
from pprint import pprint

API_Key = "cb771e45ac79a4e8e2205c0ce66ff633"#personal API from (openweather)
city = input("Enter a city: ")

base_url = "https://openweathermap.org/data/2.5/weather?appid="+API_Key+"&q"+city
weather_data = requests.get(base_url).json()
pprint(weather_data)