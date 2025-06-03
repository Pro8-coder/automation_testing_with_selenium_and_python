"""
В этом задании после нажатия кнопки страница откроется в новой вкладке,
нужно переключить WebDriver на новую вкладку и решить в ней задачу.

Сценарий для реализации выглядит так:

Открыть страницу http://suninjuly.github.io/redirect_accept.html
Нажать на кнопку
Переключиться на новую вкладку
Пройти капчу для робота и получить число-ответ
"""
import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    browser.switch_to.window(browser.window_handles[1])

    x = calc(browser.find_element(By.ID, "input_value").text)
    browser.find_element(By.ID, "answer").send_keys(x)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
finally:
    time.sleep(10)
    browser.quit()
