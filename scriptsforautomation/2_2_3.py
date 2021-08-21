from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")

    num1 = int(browser.find_element_by_css_selector("#num1").text)
    num2 = int(browser.find_element_by_css_selector("#num2").text)
    y = num1+num2
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(str(y))
    browser.find_element_by_tag_name("button").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
