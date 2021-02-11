from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/selects1.html'
browser.get(link)
try:
    num1 = browser(find_element_by_css_selector("#num1"))
    num1 = int(num1)
    num2 = browser(find_element_by_css_selector('num2'))
    num2 - int(num2)
    num3 = num2 + num1
    num3 = str(str(int(num1))+int(num2))
    browser.find_element_by_css_selector("#dropdown"),click()
    browser.find_element_by_css_selector('[value=num3]')

finally:
    time.sleep(10)
    browser.quit()


