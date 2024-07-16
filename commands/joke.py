import requests

def start():
  url = "https://official-joke-api.appspot.com/jokes/random/1"
  response = requests.get(url)
  main = [response.json()[0]["setup"], response.json()[0]["punchline"]]
  return main
