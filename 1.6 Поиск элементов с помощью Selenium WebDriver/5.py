"""
Проверьте, что можно зарегистрироваться на сайте, заполнив только обязательные
поля, отмеченные символом *: First name, last name, email. Текст для полей
может быть любым. Успешность регистрации проверяется сравнением ожидаемого
текста "Congratulations! You have successfully registered!" с текстом
на странице, которая открывается после регистрации.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    link = "http://suninjuly.github.io/registration1.html"

    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(
        By.CSS_SELECTOR,
        "[placeholder='Input your first name']"
    )
    input1.send_keys("Ivan")
    input2 = browser.find_element(
        By.CSS_SELECTOR,
        "[placeholder='Input your last name']"
    )
    input2.send_keys("Petrov")
    input3 = browser.find_element(
        By.CSS_SELECTOR,
        "[placeholder='Input your email']"
    )
    input3.send_keys("smolensk@mail.ru")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
