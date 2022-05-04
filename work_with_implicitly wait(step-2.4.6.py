from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/wait1.html")

button = browser.find_element(by=By.ID, value="verify")
button.click()
message = browser.find_element(by=By.ID, value="verify_message")

assert "successful" in message.text