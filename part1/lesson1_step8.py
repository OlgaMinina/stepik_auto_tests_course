from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    link = "https://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.first')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.second')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.third')
    input3.send_keys("petrov@gmail.com")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.quit()

try:
    link = "https://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    labels = browser.find_elements(By.TAG_NAME, 'label')
    inputs = browser.find_elements(By.TAG_NAME, 'input')

    for i, label in enumerate(labels):
        if label.text[-1] == '*':
            inputs[i].send_keys('Обязательно!')

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

    time.sleep(1)

    welcome_text = browser.find_element(By.TAG_NAME, 'h1').text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.quit()
