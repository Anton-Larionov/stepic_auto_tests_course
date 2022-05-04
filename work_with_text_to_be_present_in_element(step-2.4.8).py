from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
button = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)
browser.find_element(by=By.ID, value="book").click()
x_element = browser.find_element(by=By.ID, value="input_value").text
browser.find_element(by=By.ID, value="answer").send_keys(calc(x_element))
browser.find_element(by=By.ID, value="solve").click()
