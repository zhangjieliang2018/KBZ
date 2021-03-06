from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_driver import init_driver
from page.page import Page
from base.base_data import *


def login():
    driver = init_driver()
    page = Page(driver)
    page.login_page.input_phoneNO(phoneNo)
    page.login_page.input_smscode(smscode)
    page.login_page.click_start()
    return page, driver
