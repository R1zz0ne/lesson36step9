import pytest
import time
from selenium.webdriver.common.by import By

def test_the_presence_of_a_button(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    browser.implicitly_wait(5)
    button = len(browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket"))
    assert button == 1
    time.sleep(3)
    browser.quit()
