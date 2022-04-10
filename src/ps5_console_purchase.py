from selenium.webdriver.common.keys import Keys
from selenium import webdriver


def purchase_ps5():
    driver = webdriver.Chrome(
        "/Users/james-leightaylor/Documents/Hello World/PySelenium/PySelenium/lib/python3.9/site-packages/chromedriver2")
    driver.get("http://amazon.co.uk")
    accept_button = driver.find_element_by_id("sp-cc-accept").click()
    sign_in_button = driver.find_element_by_id(
        "nav-link-accountList-nav-line-1").click()
    email_box = driver.find_element_by_id(
        "ap_email").send_keys("jamesleight@googlemail.com")
    continue_box = driver.find_element_by_id("continue").click()
    password_box = driver.find_element_by_id(
        "ap_password").send_keys("Chelsea3521")
    sign_in_box = driver.find_element_by_id("signInSubmit").click()
    driver.get("https://www.amazon.co.uk/PlayStation-9395003-5-Console/dp/B08H95Y452/ref=sr_1_1?keywords=ps5+console&qid=1637883433&sr=8-1")
    # driver.get("https://www.amazon.co.uk/PlayStation-5-DualSense-Wireless-Controller/dp/B08H99BPJN/ref=sr_1_3?keywords=ps5+controller&qid=1637016315&sr=8-3")
    ps5_controller = driver.find_element_by_id("buy-now-button").click()
    my_address = driver.find_element_by_css_selector(
        "#address-list > div > div:nth-child(1) > div > fieldset:nth-child(1) > div.a-row.address-row.list-address-selected > span > div > label > input[type=radio]").click()
    final_address = driver.find_element_by_css_selector(
        "#orderSummaryPrimaryActionBtn > span > input").click()
    order_confirmation = driver.find_element_by_css_selector(
        "#turbo-checkout-pyo-button").click()
