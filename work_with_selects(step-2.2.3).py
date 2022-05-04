from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/selects1.html')
find_sum = str(sum([int(i.text) for i in browser.find_elements(by=By.CLASS_NAME, value="nowrap") if i.text.isdigit()]))
Select(browser.find_element(by=By.TAG_NAME, value="select")).select_by_value(find_sum)
browser.find_element(by=By.CSS_SELECTOR, value="button").click()
