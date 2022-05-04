import os
from selenium import webdriver
from selenium.webdriver.common.by import By

with open("../my_test.txt", "w", encoding="utf-8") as test:
    test.write("My education with Selenium")

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/file_input.html')
current_dir = os.path.abspath(os.path.dirname(__file__))
print(current_dir)
file_path = os.path.join(current_dir, "../my_test.txt")

options = [
    browser.find_element(by=By.CSS_SELECTOR, value="input[name='firstname']"),
    browser.find_element(by=By.CSS_SELECTOR, value="input[name='lastname']"),
    browser.find_element(by=By.CSS_SELECTOR, value="input[name='email']")
]
datas = ["Anton", "Larionov", "admin@mail.com"]
for option, data in zip(options, datas):
    option.send_keys(data)
browser.find_element(By.CSS_SELECTOR, "[type='file']").send_keys(file_path)
browser.find_element(by=By.CSS_SELECTOR, value="button").click()
