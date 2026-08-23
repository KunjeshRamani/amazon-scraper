import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.ca/Samsung-Galaxy-S26-Snapdragon-Available/dp/B0GH1GLVRJ/ref=sr_1_5?sr=8-5"

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36" }

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")

print(soup.prettify())
