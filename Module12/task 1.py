import requests
import json

try:
    request = "https://api.chucknorris.io/jokes/random"
    response = requests.get(request).json()
    print(response["value"])
except  requests.exceptions.RequestException as e:
    print("Error fetching joke:", e)

