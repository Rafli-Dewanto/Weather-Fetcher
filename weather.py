import requests
from os import system

API_KEY = "Your api key"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city: ")

request_url = f"{BASE_URL}?q={city}&appid={API_KEY}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data["weather"][0]
    description = weather["description"]
    temperature = data["main"]["temp"]
    temp_in_celcius = round(temperature - 273)
    system("clear")  # remove this line if you're using windows 
    print(f"{city.title()}\nWeather: {description}")
    print(f"Temperature: {temp_in_celcius}˚c")
else:
    print("An error occured")
