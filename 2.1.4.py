from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = ("http://suninjuly.github.io/math.html")
browser.get(link)

x_element = browser.find_element_by_css_selector("#input_value")
x = x_element.text
y = calc(x)


input = browser.find_element_by_id("answer").send_keys(y)
try:
    input = browser.find_element_by_id("answer").send_keys(y)
    input1 = browser.find_element_by_id("robotCheckbox").click()
    input2 = browser.find_element_by_id("robotsRule").click()
    input3 = browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(10)
    browser.quit()

