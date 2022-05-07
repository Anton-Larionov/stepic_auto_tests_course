import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

concat = []


@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1",
                                   "https://stepik.org/lesson/236896/step/1",
                                   "https://stepik.org/lesson/236897/step/1",
                                   "https://stepik.org/lesson/236898/step/1",
                                   "https://stepik.org/lesson/236899/step/1",
                                   "https://stepik.org/lesson/236903/step/1",
                                   "https://stepik.org/lesson/236904/step/1",
                                   "https://stepik.org/lesson/236905/step/1"])
class TestStep:
    def test_enter_in_stepik_course(self, browser, links):
        answer = math.log(int(time.time()))
        browser.get(links)
        browser.implicitly_wait(5)
        browser.find_element(By.TAG_NAME, "textarea").send_keys(answer)
        button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
        )
        button.click()
        message = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
        if "Correct!" not in message.text:
            concat.append(message.text)
        else:
            assert "Correct!"
        print(f"THIS CORRECT ANSWER: ---------> {''.join(concat)}")
