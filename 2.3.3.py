from selenium import webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(x))))
browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/alert_accept.html'
browser.get(link)

try:
    input = browser.find_element_by_css_selector(".btn").click()
    confirm=browser.switch_to.alert.accept()
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(int(x))

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    button1 = browser.find_element_by_css_selector(".btn").click()

finally:
    time.sleep(10)
    browser.quit()