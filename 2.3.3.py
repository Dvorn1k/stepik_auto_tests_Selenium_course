from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(by=By.CSS_SELECTOR, value='[name="firstname"]')
    input1.send_keys('1')

    input2 = browser.find_element(by=By.CSS_SELECTOR, value='[name="lastname"]')
    input2.send_keys("2")

    input3 = browser.find_element(by=By.CSS_SELECTOR, value='[name="email"]')
    input3.send_keys("3")

    input4 = browser.find_element(by=By.CSS_SELECTOR, value="[type='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    input4.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(by=By.CSS_SELECTOR, value="button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
