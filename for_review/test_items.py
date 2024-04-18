from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_Add_to_basket(browser):
    browser.get(link)
    time.sleep(30)
    button_basket = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    assert button_basket.is_displayed(), "Add to basket button is not displayed on the website"



