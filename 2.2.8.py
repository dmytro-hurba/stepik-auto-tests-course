from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/file_input.html'
browser.get(link)

try:
    input1 = browser.find_element_by_css_selector("[name='firstname']").send_keys('ivan')
    input2 = browser.find_element_by_css_selector("[name = 'lastname']").send_keys('re')
    input3 = browser.find_element_by_css_selector("[name='email']").send_keys('dds')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file_example.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)
    button1 = browser.find_element_by_css_selector(".btn").click()

finally:
    time.sleep(5)
    browser.quit()