"""
В этой задаче вам нужно написать программу, которая будет выполнять следующий
сценарий:

Открыть страницу http://suninjuly.github.io/alert_accept.html
Нажать на кнопку
Принять confirm
На новой странице решить капчу для роботов, чтобы получить число с ответом
"""
import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    confirm = browser.switch_to.alert
    confirm.accept()

    time.sleep(1)

    x = calc(browser.find_element(By.ID, "input_value").text)
    browser.find_element(By.ID, "answer").send_keys(x)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
finally:
    time.sleep(10)
    browser.quit()
