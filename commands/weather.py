# weather
import requests
from constants import rapid_key


def weather_response(city):
    url = f"https://open-weather13.p.rapidapi.com/city/{city}/EN"
    headers = {
        "x-rapidapi-key": f"{rapid_key}",
        "x-rapidapi-host": "open-weather13.p.rapidapi.com"
    }
    try:
        response = requests.get(url, headers=headers)
        response = response.json()
        return response
    except Exception as e:
        output = f"Error: {e} \n\nPlease try again later"
        return output
