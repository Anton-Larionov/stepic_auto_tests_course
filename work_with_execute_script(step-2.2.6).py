from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get('http://SunInJuly.github.io/execute_script.html')
browser.execute_script("window.scrollBy(0, 150);")
find_x = browser.find_element(by=By.ID, value="input_value").text
browser.find_element(by=By.ID, value="answer").send_keys(calc(find_x))
elements_for_click = [browser.find_element(by=By.ID, value="robotCheckbox"),
                      browser.find_element(by=By.ID, value="robotsRule"),
                      browser.find_element(by=By.CSS_SELECTOR, value="button")
                      ]
for element in elements_for_click:
    element.click()
