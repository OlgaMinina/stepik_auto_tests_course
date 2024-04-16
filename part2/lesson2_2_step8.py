from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

link = "https://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element(By.CSS_SELECTOR, 'input[name = "firstname"]').send_keys("Olga")
browser.find_element(By.CSS_SELECTOR, 'input[name = "lastname"]').send_keys("O")
browser.find_element(By.CSS_SELECTOR, 'input[name = "email"]').send_keys("olga.o@gmail.com")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, "file.txt")
element = browser.find_element(By.CSS_SELECTOR, 'input[type = "file"]')
element.send_keys(file_path)

browser.find_element(By.CSS_SELECTOR, 'button[type = "submit"]').click()
time.sleep(5)
browser.quit()
