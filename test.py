import requests
from bs4 import BeautifulSoup

url = "https://www.bestbuy.ca/en-ca/product/apple-macbook-neo-13-2026-silver-apple-a18-pro-8gb-ram-256gb-ssd-english/19791903"

response = requests.get(url)

print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

print(soup.title.get_text(strip=True))
