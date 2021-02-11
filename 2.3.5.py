from selenium import webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(x))))
browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/redirect_accept.html'
browser.get(link)
input = browser.find_element_by_css_selector('button').click()
new_page = browser.window_handles[1]
browser.switch_to.window(new_page)
x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(int(x))

input2 = browser.find_element_by_id("answer").send_keys(y)


button1 = browser.find_element_by_css_selector(".btn").click()
