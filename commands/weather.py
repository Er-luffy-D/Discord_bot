# weather
import requests


def weather_response(city):
    url = f"https://open-weather13.p.rapidapi.com/city/{city}/EN"
    headers = {
        "x-rapidapi-key": "49ea0f74e0mshd8194fee70e06d9p10071fjsna5e143eb6977",
        "x-rapidapi-host": "open-weather13.p.rapidapi.com"
    }
    try:
        response = requests.get(url, headers=headers)
        response = response.json()
        return response
    except Exception as e:
        output = f"Error: {e} \n\nPlease try again later"
        return output
