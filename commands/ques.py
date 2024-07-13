import google.generativeai as genai
import os


def _get_api_key():
  return os.getenv("api_key")


genai.configure(api_key=os.environ["api"])
model = genai.GenerativeModel('gemini-1.5-flash')


def shorten(text):
  end = text.rfind(".", 0, 2000)
  text = text[:end + 1]
  return text


def ans(text):
  try:
    response = model.generate_content(text)
    res_tex = response.text
  except Exception as e:
    return f"Error found Try again . If it persists contact the owner. \n{e}"
  if len(res_tex) >= 1950:
    res_tex = shorten(res_tex)
    print(len(res_tex))
    return res_tex
  print(len(res_tex))
  return res_tex
