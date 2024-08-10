from AnilistPython import Anilist
import requests


def ongoing():
  response = requests.get("https://myanimelist.net/anime/season")
  # response = response.json()
  return response.content


def search(anime_name):
  anime = Anilist()
  return anime.get_anime(anime_name)


if __name__ == "__main__":
  print(ongoing())
