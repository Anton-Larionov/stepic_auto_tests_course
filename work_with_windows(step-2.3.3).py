from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/alert_accept.html')
browser.find_element(by=By.CSS_SELECTOR, value="button").click()
browser.switch_to.alert.accept()
find_x = int([i.text for i in browser.find_elements(by=By.CLASS_NAME, value="nowrap")][-1])
browser.find_element(by=By.ID, value="answer").send_keys(calc(find_x))
browser.find_element(by=By.CSS_SELECTOR, value="button").click()
