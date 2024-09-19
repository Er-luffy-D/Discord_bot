from AnilistPython import Anilist
import requests
from bs4 import BeautifulSoup


def current():
  response = requests.get("https://myanimelist.net/anime/season")
  soup = BeautifulSoup(response.text, 'html.parser')
  name = soup.find_all("a", class_='link-title')
  name = [i.text for i in name]
  date = soup.find_all("div", class_='info')
  date = [i.find_all("span", class_='item')[0].text for i in date]
  anime_list = [f"{(name[i])}_{date[i]}" for i in range(len(name))]

  return anime_list[:10]


def search(anime_name):
  anime = Anilist()
  try:
    anime_dict = anime.get_anime(anime_name)
    return anime_dict
  except:
    return -1

  # working on this
  # eng_name = anime_dict['name_english']
  # rom_name = anime_dict['name_romaji']
  # start_time = anime_dict['starting_time']
  # end_time = anime_dict['ending_time']
  # cover_img = anime_dict['cover_image']
  # airing_st = anime_dict['airing_status']
  # episodes = anime_dict['airing_episodes']

  # desc = anime_dict['desc']


if __name__ == "__main__":
  for x, y in search("naruto").items():
    print(x, y)
    print()
