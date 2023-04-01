import time
from selenium.webdriver.common.by import By


url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_add(browser):
    browser.get(url)
    time.sleep(10)
    button_add_to_cart = browser.find_element(By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    assert button_add_to_cart, "Button not found"

