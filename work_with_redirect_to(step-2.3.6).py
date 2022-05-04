from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/redirect_accept.html')
browser.find_element(by=By.CSS_SELECTOR, value="button").click()
browser.switch_to.window(browser.window_handles[1])
x = browser.find_element(by=By.ID, value="input_value").text
browser.find_element(by=By.ID, value="answer").send_keys(calc(x))
browser.find_element(by=By.CSS_SELECTOR, value="button").click()
