"""
Напишите код, который реализует следующий сценарий:

Открыть страницу https://suninjuly.github.io/selects1.html
Посчитать сумму заданных чисел
Выбрать в выпадающем списке значение равное расчитанной сумме
Нажать кнопку "Submit"

Если все сделано правильно и достаточно быстро (в этой задаче тоже есть
ограничение по времени), вы увидите окно с числом. Отправьте полученное число
в качестве ответа для этого задания.

Когда ваш код заработает, попробуйте запустить его на странице
https://suninjuly.github.io/selects2.html. Ваш код и для нее тоже должен
пройти успешно.
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


try:
    link = "https://suninjuly.github.io/selects1.html"
    # link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1")
    num2 = browser.find_element(By.ID, "num2")

    browser.find_element(By.ID, "dropdown").click()

    Select(
        browser.find_element(By.TAG_NAME, "select")
    ).select_by_visible_text(f"{int(num1.text) + int(num2.text)}")

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
finally:
    time.sleep(10)
    browser.quit()
