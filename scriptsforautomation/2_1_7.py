from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    x_element = browser.find_element_by_css_selector("#treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    answer_locator = browser.find_element_by_css_selector("#answer")
    answer_locator.send_keys(y)
    i_am_robot_checkbox_locator = browser.find_element_by_css_selector("#robotCheckbox")
    i_am_robot_checkbox_locator.click()
    robotsRule_radiobutton_locator = browser.find_element_by_css_selector("#robotsRule")
    robotsRule_radiobutton_locator.click()
    submit_button_locator = browser.find_element_by_css_selector(".btn.btn-default")
    submit_button_locator.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
