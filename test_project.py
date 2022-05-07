import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_url(url):
    browser = webdriver.Chrome()
    browser.get(url)
    elements = [
        browser.find_element(By.CSS_SELECTOR,
                             "div.first_block input.first"),
        browser.find_element(By.CSS_SELECTOR,
                             "div.first_block input.second"),
        browser.find_element(By.CSS_SELECTOR,
                             "div.first_block input.third")
    ]
    for element in elements:
        element.send_keys("Required")
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    browser.quit()
    return welcome_text


class TestRegistration(unittest.TestCase):
    def test_registration_1(self):
        text = get_url("http://suninjuly.github.io/registration1.html")
        self.assertEqual(text, "Congratulations! You have successfully registered!")

    def test_registration_2(self):
        text = get_url("http://suninjuly.github.io/registration2.html")
        self.assertEqual(text, "Congratulations! You have successfully registered!")


if __name__ == "__main__":
    unittest.main()
