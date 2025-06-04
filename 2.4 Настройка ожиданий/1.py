"""
Тестовый сценарий выглядит так:

Открыть страницу http://suninjuly.github.io/wait1.html
Нажать на кнопку "Verify" (на данной странице пауза перед появлением кнопки
установлена на 1 секунду)
Проверить, что появилась надпись "Verification was successful!"
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/wait1.html")

    browser.find_element(By.ID, "verify").click()
    message = browser.find_element(By.ID, "verify_message")

    assert message.text == "Verification was successful!"
finally:
    time.sleep(10)
    browser.quit()
