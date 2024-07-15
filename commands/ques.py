import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import os


def _get_api_key():
  return os.getenv("api_key")


genai.configure(api_key=os.environ["api"])
model = genai.GenerativeModel('gemini-1.5-flash')


def ans(text):
  try:
    response = model.generate_content(
        text)
    res_tex = response.text
  except Exception as e:
    return f"Error found Try again . If it persists contact the owner. \n{e}"
  return res_tex
