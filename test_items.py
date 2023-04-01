import time
import pytest
from selenium import webdriver


url = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"


def test_button_add(browser):
    browser.get(url)
    time.sleep(20)

