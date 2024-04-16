from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x = browser.find_element(By.CSS_SELECTOR, 'span[id="input_value"]').text
y = calc(x)


answer = browser.find_element(By.CSS_SELECTOR, 'input[id="answer"]')
browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
answer.send_keys(y)
robot_checkbox = browser.find_element(By.CSS_SELECTOR, 'input[id="robotCheckbox"]')
browser.execute_script("return arguments[0].scrollIntoView(true);", robot_checkbox)
robot_checkbox.click()
browser.find_element(By.CSS_SELECTOR, 'input[id="robotsRule"]').click()
button = browser.find_element(By.TAG_NAME, 'button')
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

time.sleep(5)



