from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    browser = webdriver.Chrome()
#    browser.get("http://suninjuly.github.io/selects1.html")
#    browser.execute_script("alert('Robots at work');")
#    browser.execute_script("document.title='Script executing';")
    browser.execute_script("document.title='Script executing';alert('Robots at work');")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
