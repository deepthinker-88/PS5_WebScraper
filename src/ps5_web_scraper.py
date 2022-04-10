import smtplib
from bs4 import BeautifulSoup
import requests

item_name_to_url = {
    "PS5 Controller": "https://www.amazon.co.uk/PlayStation-5-DualSense-Wireless-Controller/dp/B08H99BPJN/ref=sr_1_4?keywords=ps5+controller&qid=1637853787&sr=8-4",
    "PS5 Console": "https://www.amazon.co.uk/PlayStation-9395003-5-Console/dp/B08H95Y452/ref=sr_1_1?dchild=1&keywords=ps5&qid=1633424672&sr=8-1"
}


def get_page_html(item_name):
    url = item_name_to_url[item_name]
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"}
    page = requests.get(url, headers=headers)
    return page.content


def check_item_in_stock(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    available_to_buy = soup.find(
        "input", {"id": "buy-now-button"},)
    return available_to_buy is not None


def check_inventory(page_html):
    item_name_to_url = "https://www.amazon.co.uk/PlayStation-5-DualSense-Wireless-Controller/dp/B08H99BPJN/ref=sr_1_4?keywords=ps5+controller&qid=1637853787&sr=8-4"
    item_name_to_url = "https://www.amazon.co.uk/PlayStation-9395003-5-Console/dp/B08H95Y452/ref=sr_1_1?dchild=1&keywords=ps5&qid=1633822707&sr=8-1"
    page_html = get_page_html
    if check_item_in_stock(page_html):
        print("In stock")
        send_mail()
    else:
        print("Out of stock")
        send_mail()


def check_for_ps5():
    item_name = "PS5 Controller"
    item_html = get_page_html(item_name)
    item_in_stock = check_item_in_stock(item_html)

    if item_in_stock:
        send_mail()
    return item_in_stock


if __name__ == "__main__":
    check_for_ps5()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("jamesleight@googlemail.com", "bvpcodlqxkuhdppx")

    subject = "PS5 Update"
    body = "Congratulations James-Leigh, the PS5 Controller is in stock and has been ordered on your behalf!!! "
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail("jamesleight@googlemail.com",
                    "jamesleight@googlemail.com", msg
                    )
