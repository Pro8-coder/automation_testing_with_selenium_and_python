"""
Напишите скрипт, который будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/file_input.html
Заполнить текстовые поля: имя, фамилия, email
Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
Нажать кнопку "Submit"
"""
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(
        By.CSS_SELECTOR, "[name='firstname']").send_keys("Ivan")

    browser.find_element(
        By.CSS_SELECTOR, "[name='lastname']").send_keys("Petrov")

    browser.find_element(
        By.CSS_SELECTOR, "[name='email']").send_keys("smolensk@mail.ru")

    element = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, '3.txt')
    element.send_keys(file_path)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
finally:
    time.sleep(10)
    browser.quit()
