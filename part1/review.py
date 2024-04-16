from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def get_chromedriver():
    chrom_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrom_options)
    return driver


def main():
    try:
        driver = get_chromedriver()
        driver.get('https://suninjuly.github.io/registration1.html')

        fn = driver.find_element(By.CLASS_NAME, "first")
        fn.send_keys("Abrasha")

        ln = driver.find_element(By.CLASS_NAME, "second")
        ln.send_keys("Maizl")

        email = driver.find_element(By.CLASS_NAME, "third")
        email.send_keys("Abracadabra@gmail.com")

        phone = driver.find_element(By.XPATH, '//input[@placeholder="Input your phone:"]')
        phone.send_keys("+79998789980")

        address = driver.find_element(By.XPATH, '//input[@placeholder="Input your address:"]')
        address.send_keys('parapaparam 12')

        driver.find_element(By.CLASS_NAME, "btn").click()

        time.sleep(3)

        congr = driver.find_element(By.TAG_NAME, "h1").text
        assert "Congratulations! You have successfully registered!" == congr


    finally:
        driver.quit()



if __name__ == '__main__':
    main()
