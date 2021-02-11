from selenium import webdriver
import time
import math

def calc(input1):
  return str(math.log(abs(12*math.sin(int(input1)))))

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/get_attribute.html'
browser.get(link)
try:
    input = browser.find_element_by_css_selector('#treasure')
    input1 = input.get_attribute('valuex')
    y = calc(input1)
    input2 = browser.find_element_by_css_selector("#answer").send_keys(y)
    input3 = browser.find_element_by_id("robotCheckbox").click()
    input4 = browser.find_element_by_id("robotsRule").click()
    input5 = browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(15)
    browser.quit()

