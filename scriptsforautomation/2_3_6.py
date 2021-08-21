from selenium import webdriver
import time
import os
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    browser.find_element_by_css_selector(".trollface.btn").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_loc = browser.find_element_by_id("input_value")
    x = x_loc.text
    browser.find_element_by_id("answer").send_keys(calc(x))
    browser.find_element_by_class_name("btn-primary").click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
