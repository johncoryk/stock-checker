import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.roguefitness.com/the-rogue-bar-2-0'

headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

time_check = 60*120


def check_status():
    if soup.find_all(title="Qty"):
        print('It is here')
        send_mail()
    else:
        print('it is not here')


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('myemail@email.com',
                 'randomPassword')

    subject = 'Rogue Bar in stock'
    body = 'Check the link, the bar is in stock, but not for long! https://www.roguefitness.com/the-rogue-bar-2-0'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'coryk0789@gmail.com',
        ['coryk0789@gmail.com', 'emilyfaucher0827@gmail.com'],
        msg
    )

    print('EMAIL SENT!')

    server.quit()


while(True):
    check_status()
    time.sleep(time_check)
