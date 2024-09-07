import os
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from dotenv import load_dotenv
load_dotenv()
MY_EMAIL = os.getenv('MY_EMAIL')
MY_PASSWORD = os.getenv('MY_PASSWORD')
MY_PATH = os.getenv("MY_PATH")


def purchase_ps5():
    driver = webdriver.Chrome(
        MY_PATH)
    driver.get("http://amazon.co.uk")
    accept_button = driver.find_element_by_id("sp-cc-accept").click()
    sign_in_button = driver.find_element_by_id(
        "nav-link-accountList-nav-line-1").click()
    email_box = driver.find_element_by_id(
        "ap_email").send_keys(MY_EMAIL)
    continue_box = driver.find_element_by_id("continue").click()
    password_box = driver.find_element_by_id(
        "ap_password").send_keys(MY_PASSWORD)
    sign_in_box = driver.find_element_by_id("signInSubmit").click()
    driver.get("https://www.amazon.co.uk/PlayStation-9395003-5-Console/dp/B08H95Y452/ref=sr_1_1?keywords=ps5+console&qid=1637883433&sr=8-1")
    ps5_controller = driver.find_element_by_id("buy-now-button").click()
    my_address = driver.find_element_by_css_selector(
        "#address-list > div > div:nth-child(1) > div > fieldset:nth-child(1) > div.a-row.address-row.list-address-selected > span > div > label > input[type=radio]").click()
    final_address = driver.find_element_by_css_selector(
        "#orderSummaryPrimaryActionBtn > span > input").click()
    order_confirmation = driver.find_element_by_css_selector(
        "#turbo-checkout-pyo-button").click()


def purchase_ps5_controller():
    driver = webdriver.Chrome(
        "/Users/james-leightaylor/Desktop/PS5_Project/PS5/src/chromerdriver\ 2.exe")
    driver.get("http://amazon.co.uk")
    accept_button = driver.find_element_by_id("sp-cc-accept").click()
    sign_in_button = driver.find_element_by_id(
        "nav-link-accountList-nav-line-1").click()
    email_box = driver.find_element_by_id(
        "ap_email").send_keys(MY_EMAIL)
    continue_box = driver.find_element_by_id("continue").click()
    password_box = driver.find_element_by_id(
        "ap_password").send_keys(MY_PASSWORD)
    sign_in_box = driver.find_element_by_id("signInSubmit").click()
    driver.get("https://www.amazon.co.uk/PlayStation-5-DualSense-Wireless-Controller/dp/B08H99BPJN/ref=sr_1_3?keywords=ps5+controller&qid=1637016315&sr=8-3")
    ps5_controller = driver.find_element_by_id("buy-now-button").click()
    my_address = driver.find_element_by_css_selector(
        "#address-list > div > div:nth-child(1) > div > fieldset:nth-child(1) > div.a-row.address-row.list-address-selected > span > div > label > input[type=radio]").click()
    final_address = driver.find_element_by_css_selector(
        "#orderSummaryPrimaryActionBtn > span > input").click()
    order_confirmation = driver.find_element_by_css_selector(
        "#turbo-checkout-pyo-button").click()
    