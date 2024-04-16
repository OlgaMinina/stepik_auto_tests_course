from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value("41")
select.select_by_visible_text("41")