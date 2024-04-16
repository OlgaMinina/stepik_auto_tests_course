import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
button = browser.find_element(By.ID, 'book')
button.click()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x = browser.find_element(By.CSS_SELECTOR, 'span[id="input_value"]').text
y = calc(x)

browser.find_element(By.CSS_SELECTOR, 'input[id="answer"]').send_keys(y)
browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

time.sleep(5)
browser.quit()
