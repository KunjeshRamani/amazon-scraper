import requests
from bs4 import BeautifulSoup
import smtplib
import time

def send_email():
    # GMail Specific
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("kunjeshramani55@gmail.com", "ksecegtzlwpifdcx")

    subject = "Price Fell Down!!!!!"
    body = "Check out the Link ASAP\n\nhttps://www.amazon.ca/Samsung-Galaxy-Book4-Edge-Fingerprint/dp/B0HBB6FYDR/ref=sr_1_1_sspa?sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('kunjeshramani55@gmail.com', "kunjeshramani55@gmail.com", msg)
    print("EMAIL is SENT")

    server.quit()



# "my user agent" google it
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/151.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-CA,en;q=0.9",
}


# URL = "https://www.amazon.ca/Samsung-Galaxy-Book4-Edge-Fingerprint/dp/B0HBB6FYDR/ref=sr_1_1_sspa?sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY"
URL = "https://www.walmart.ca/en/ip/Beats-Solo-4-True-Wireless-On-Ear-Headphones-Re-engineered-acoustics-Ultralight-ergonomic-design-Compatible-Apple-Android-Class-1-Bluetooth/3UXPXT4ICZ1C?fulfillmentIntent=Pickup&filters=%5B%7B%22intent%22%3A%22fulfillmentIntent%22%2C%22values%22%3A%5B%22Pickup%22%5D%7D%5D&classType=VARIANT&from=/search"

def amazon_scraper(url):
    page = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find("span", id="productTitle").get_text()
    price = soup.find("span", class_="a-price-whole").get_text()
    price_character_needed = price[:5]
    price_remove_comma = price_character_needed.replace(",", "")
    price_number = float(price_remove_comma)

    print(title.strip())
    print(price_number)

    if price_number < 1400.00:
         send_email()

def walmart_scraper(url):
    page = requests.get(url, headers=HEADERS, timeout=10)

    print("Status:", page.status_code)
    print("Length:", len(page.text))

    with open("walmart_response.html", "w", encoding="utf-8") as f:
        f.write(page.text)

    soup = BeautifulSoup(page.text, "html.parser")

    print("Title:", soup.find("h1", id="main-title"))

    print("Beats" in page.text)
    print("main-title" in page.text)
    print("Access Denied" in page.text)

    with open("walmart_response.html", "w", encoding="utf-8") as f:
        f.write(page.text)

    print("Saved to walmart_response.html")

walmart_scraper(URL)
