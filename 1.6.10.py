from selenium import webdriver
import  time
link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
try:
    browser.get(link)
    input1 = browser.find_element_by_css_selector(".form-control.first").send_keys("Gaben")
    input2 = browser.find_element_by_css_selector(".form-control.second").send_keys("Newel")
    input3 = browser.find_element_by_css_selector(".form-control.third").send_keys("gaben@gmail.com")
    button = browser.find_element_by_css_selector(".btn").click()
    time.sleep(5)
    expected_result = browser.find_element_by_tag_name("h1")
    welcome_text = expected_result.text

    assert "Congratulations! You have successfully registered!" == expected_result


finally:
    time.sleep(15)
    browser.quit()