import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


class TestFormulaStepic():
    stepik_links = ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
                    "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
                    "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
                    "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"]

    @pytest.mark.parametrize('links', stepik_links)
    def test_time_formula(self, browser, links):
        browser.get(links)

        login = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.navbar__auth_login')))
        login.click()
        browser.find_element(By.CSS_SELECTOR, 'input[name="login"]').send_keys("olyaminina1@gmail.com")
        browser.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys("Mongobongo891")
        browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        time.sleep(6)

        # solve_again = browser.find_element(By.CSS_SELECTOR, 'button[class="again-btn white"]')

        text_area = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.TAG_NAME, 'textarea')))
        text_area.send_keys(str(math.log(int(time.time()))))

        submit = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@class="submit-submission"]')))
        submit.click()

        correct_word = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'p[class="smart-hints__hint"]')))

        assert correct_word.text == "Correct!", "The message is different"
