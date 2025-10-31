import requests
import json

city = input("Enter the name of a municipality: ")

try:
    api_key = "c141f730802dc35ed7a9a423396ced03"
    request =  f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(request).json()

    temp_kelvin = response["main"]["temp"]
    description = response["weather"][0]["description"]
    temp_celsius = temp_kelvin - 273.15

    print(f"Weather in {city}: {description}")
    print(f"Temperature: {temp_celsius:.1f}°C")

except KeyError:
    print("Unexpected format. Please check the city name or API key.")
