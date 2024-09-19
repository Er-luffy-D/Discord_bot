import requests


def git(username):
  response = requests.get(f"https://api.github.com/users/{username}")
  if response.status_code == 200:
    data = response.json()
    return data
  else:
    return None


if __name__ == "__main__":
  print(git("Er-luffy-D"))
