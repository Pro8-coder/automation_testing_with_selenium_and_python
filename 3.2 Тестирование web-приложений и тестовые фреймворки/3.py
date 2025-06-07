"""
Попробуйте оформить тесты из первого модуля в стиле unittest.

Возьмите тесты из шага — 1.6 Поиск элементов с помощью Selenium WebDriver
Создайте новый файл
Создайте в нем класс с тестами, который должен наследоваться от
unittest.TestCase по аналогии с предыдущим шагом
Перепишите в стиле unittest тест для страницы
http://suninjuly.github.io/registration1.html
Перепишите в стиле unittest второй тест для страницы
http://suninjuly.github.io/registration2.html
Оформите финальные проверки в тестах в стиле unittest, например, используя
проверочный метод assertEqual
Запустите получившиеся тесты из файла
Просмотрите отчёт о запуске и найдите последнюю строчку
Отправьте эту строчку в качестве ответа на это задание
Обратите внимание, что по задумке должно выбрасываться исключение
NoSuchElementException во втором тесте. Если вы использовали конструкцию
try/except, здесь нужно запустить тест без неё. Ловить исключения не надо
(во всяком случае, здесь)!

Это всё для иллюстрации того, что unittest выполнит тесты и обобщит результаты
даже при наличии неожиданного исключения.
"""
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()

    def test_registration1(self, ):
        self.browser.get("http://suninjuly.github.io/registration1.html")

        self.browser.find_element(
            By.CSS_SELECTOR,
            "[required].first"
        ).send_keys("Ivan")

        self.browser.find_element(
            By.CSS_SELECTOR,
            "[required].second"
        ).send_keys("Petrov")

        self.browser.find_element(
            By.CSS_SELECTOR,
            "[required].third"
        ).send_keys("smolensk@mail.ru")

        self.browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        welcome_text = self.browser.find_element(By.TAG_NAME, "h1").text

        self.assertEqual(
            "Congratulations! You have successfully registered!",
            welcome_text,
            "Текст приветствия не соответствует ожидаемому"
        )

    def test_registration2(self):
        self.browser.get("http://suninjuly.github.io/registration2.html")

        self.browser.find_element(
            By.CSS_SELECTOR,
            "[required].first"
        ).send_keys("Ivan")

        self.browser.find_element(
            By.CSS_SELECTOR,
            "[required].second"
        ).send_keys("Petrov")

        self.browser.find_element(
            By.CSS_SELECTOR,
            "[required].third"
        ).send_keys("smolensk@mail.ru")

        self.browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        welcome_text = self.browser.find_element(By.TAG_NAME, "h1").text

        self.assertEqual(
            "Congratulations! You have successfully registered!",
            welcome_text,
            "Текст приветствия не соответствует ожидаемому"
        )


if __name__ == "__main__":
    unittest.main()
