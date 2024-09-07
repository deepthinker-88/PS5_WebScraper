import os
import smtplib
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
load_dotenv()
MY_EMAIL = os.getenv('MY_EMAIL')
SERVER_PASSWORD = os.getenv('SERVER_PASSWORD')

ps5_console_item_name_to_url = {
"PS5 Console": "https://www.amazon.co.uk/PlayStation-9395003-5-Console/dp/B08H95Y452/ref=sr_1_1?dchild=1&keywords=ps5&qid=1633424672&sr=8-1"
}
ps5_controller_item_name_to_url = {
    "PS5 Controller": "https://www.amazon.co.uk/PlayStation-5-DualSense-Wireless-Controller/dp/B08H99BPJN/ref=sr_1_4?keywords=ps5+controller&qid=1637853787&sr=8-4"}



# function that returns html page of PS5 Console
def get_ps5_console_page_html(item_name):
    url = ps5_console_item_name_to_url[item_name]
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"}
    page = requests.get(url, headers=headers)
    return page.content

# function that returns html page of PS5 Controller
def get_ps5_controller_page_html(item_name):
    url = ps5_controller_item_name_to_url[item_name]
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"}
    page = requests.get(url, headers=headers)
    return page.content


# function that scrapes the ps5 webpage
def ps5_console_controller_webscraping(page_html):
    soup = BeautifulSoup(page_html,'html.parser')
    available_to_buy = soup.find(
    "input", {"id": "buy-now-button"},   
    )
    return available_to_buy is not None


# function that checks if PS5 Console is available/unavailable - sends e-mail depending on the outcome
def check_if_ps5_console_is_available():
    item_name = "PS5 Console"
    item_in_stock = get_ps5_console_page_html(item_name)
    item_not_in_stock = get_ps5_console_page_html(item_name)
    

    if item_in_stock:
        print("PS5 Console is available on Amazon")
        send_ps5_console_mail_if_in_stock()
    elif item_not_in_stock:
        print("Sorry, the Ps5 Console is unavailable")
        send_ps5_console_mail_if_not_in_stock()
    return item_in_stock
    

# function that sends e-mail
def send_ps5_console_mail_if_in_stock():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(MY_EMAIL, SERVER_PASSWORD)

    subject = "PS5 Console Update"
    body = "Congratulations James-Leigh, the PS5 Console is in stock on Amazon "
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(MY_EMAIL,
                    MY_EMAIL, msg
                    )


# function that sends e-mail
def send_ps5_console_mail_if_not_in_stock():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(MY_EMAIL)

    subject = "PS5 Console Update"
    body = "Unfortunately James-Leigh, the PS5 Console is not in stock, will try again later!!! "
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(MY_EMAIL,
                    MY_EMAIL, msg
                    )



# function that checks if PS5 Controller is available/unavailable - sends e-mail depending on the outcome
def check_if_ps5_controller_is_available():
    item_name = "PS5 Controller"
    item_in_stock = get_ps5_controller_page_html(item_name)
    item_not_in_stock = get_ps5_controller_page_html(item_name)
    if item_in_stock:
        print("Ps5 Controller is in stock!!")
        send_ps5_controller_mail_if_available_online()
        
    elif item_not_in_stock:
        send_ps5_controller_mail_if_not_in_stock()
    
        

# function that sends e-mail
def send_ps5_controller_mail_if_available_online():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(MY_EMAIL, SERVER_PASSWORD)

    subject = "PS5 Controller Update"
    body = "Congratulations James-Leigh, the PS5 Controller is in stock !!! "
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(MY_EMAIL,
                    MY_EMAIL, msg
                    )


# function that sends e-mail
def send_ps5_controller_mail_if_not_in_stock():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(MY_EMAIL, SERVER_PASSWORD)

    subject = "PS5 Controller Update"
    body = "Unfortunately James-Leigh, the PS5 Controller is not in stock, will try again later !!! "
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail("jamesleight@googlemail.com",
                    "jamesleight@googlemail.com", msg
                    )



if __name__ == "__main__":
    check_if_ps5_console_is_available()
    check_if_ps5_controller_is_available()
