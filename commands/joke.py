import requests
import random
from constants import rapid_key


def joke_res():
  x = random.randint(1, 2)
  try:
    if x == 1:
      url = "https://bestjokeapi.p.rapidapi.com/jokes/produce"
      headers = {
          "x-rapidapi-key": f"{rapid_key}",
          "x-rapidapi-host": "bestjokeapi.p.rapidapi.com"
      }
      response = requests.get(url, headers=headers)
      main = [response.json()["joke"]]
      return main

    else:
      url = "https://dad-jokes-by-api-ninjas.p.rapidapi.com/v1/dadjokes"

      headers = {
          "x-rapidapi-key": f"{rapid_key}",
          "x-rapidapi-host": "dad-jokes-by-api-ninjas.p.rapidapi.com"
      }

      response = requests.get(url, headers=headers)

      main = [response.json()[0]["joke"]]
      return main

  except Exception as e:
    return f"Error: {e} \n\nPlease try again later"
