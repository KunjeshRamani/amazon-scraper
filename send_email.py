import smtplib

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
