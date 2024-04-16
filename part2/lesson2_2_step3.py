from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

x = int(browser.find_element(By.CSS_SELECTOR, 'span[id ="num1"]').text)
y = int(browser.find_element(By.CSS_SELECTOR, 'span[id ="num2"]').text)
value = str(x + y)

select = Select(browser.find_element(By.TAG_NAME, 'select'))
select.select_by_value(value)
browser.find_element(By.CSS_SELECTOR, 'button[type ="submit"]').click()

time.sleep(5)
browser.quit()
