from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
confirm = browser.switch_to.alert
confirm.accept()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x = browser.find_element(By.CSS_SELECTOR, 'span[id="input_value"]').text
y = calc(x)

browser.find_element(By.CSS_SELECTOR, 'input[id="answer"]').send_keys(y)
browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

time.sleep(5)
browser.quit()