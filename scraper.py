import requests
from bs4 import BeautifulSoup
import smtplib
import time


def send_email():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("kunjeshramani55@gmail.com", "yrvqpckxdexiwdwk")

    subject = "Price Fell Down!!!!!"
    body = "Check the amazon.ca link https://www.amazon.ca/Samsung-Galaxy-Book4-Edge-Fingerprint/dp/B0HBB6FYDR/ref=sr_1_1_sspa?sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY"

    msg = f"Subject: {subject}\n\n Body: {body}"

    server.sendmail('kunjeshramani55@gmail.com', "kunjeshramani55@gmail.com", msg)
    print("EMAIL is SENT")

    server.quit()


URL = "https://www.amazon.ca/Samsung-Galaxy-Book4-Edge-Fingerprint/dp/B0HBB6FYDR/ref=sr_1_1_sspa?sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY"

# "my user agent" google it
headers = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/151.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-CA,en;q=0.9",
}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find("span", id="productTitle").get_text()
price = soup.find("span", class_="a-price-whole").get_text()
price_character_needed = price[:5]
price_remove_comma = price_character_needed.replace(",","")
price_number = float(price_remove_comma)

print(title.strip())
print(price_number)


if price_number < 1400.00:
    send_email()
#
# while(True):
#     check_price()
#     time.sleep(60*60)
