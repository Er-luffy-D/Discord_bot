import google.generativeai as genai
import os


def _get_api_key():
  return os.getenv("api_key")


genai.configure(api_key=os.environ["api"])
model = genai.GenerativeModel('gemini-1.5-flash')


def ans(text):
  response = model.generate_content(text)
  return response.text
