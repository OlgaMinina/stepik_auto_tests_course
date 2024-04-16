from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.CSS_SELECTOR, 'span[id="input_value"]')
x = x_element.text
y = calc(x)

browser.find_element(By.CSS_SELECTOR, 'input[id = "answer"]').send_keys(y)
browser.find_element(By.CSS_SELECTOR, 'input[id = "robotCheckbox"]').click()
browser.find_element(By.CSS_SELECTOR, '[for = "robotsRule"]').click()
browser.find_element(By.CSS_SELECTOR, 'button[type = "submit"]').click()

time.sleep(5)

browser.quit()





