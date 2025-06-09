"""
Инопланетяне оставляют загадочные сообщения на Stepik в фидбеке задач на
правильное решение. Мы смогли локализовать несколько url-адресов задач, где
появляются кусочки сообщений. Ваша задача — реализовать автотест со следующим
сценарием действий:

открыть страницу
авторизоваться на странице со своим логином и паролем (см. предыдущий шаг)
ввести правильный ответ (поле перед вводом должно быть пустым)
нажать кнопку "Отправить"
дождаться фидбека о том, что ответ правильный
проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"
Опциональный фидбек — это текст в черном поле, как показано на скриншоте:

Правильным ответом на задачу в заданных шагах является число:

import time
import math

answer = math.log(int(time.time()))
Используйте маркировку pytest для параметризации и передайте в тест список
ссылок в качестве параметров:

https://stepik.org/lesson/236895/step/1
https://stepik.org/lesson/236896/step/1
https://stepik.org/lesson/236897/step/1
https://stepik.org/lesson/236898/step/1
https://stepik.org/lesson/236899/step/1
https://stepik.org/lesson/236903/step/1
https://stepik.org/lesson/236904/step/1
https://stepik.org/lesson/236905/step/1

Используйте осмысленное сообщение об ошибке в проверке текста, а также
настройте нужные ожидания, чтобы тесты работали стабильно.

В упавших тестах найдите кусочки послания. Тест должен падать, если текст
в опциональном фидбеке не совпадает со строкой "Correct!" Соберите кусочки
текста в одно предложение и отправьте в качестве ответа на это задание.

Важно! Чтобы пройти это задание, дополнительно убедитесь в том, что у вас
установлено правильное локальное время (https://time.is/ru/). Ответ для каждой
задачи нужно пересчитывать отдельно, иначе они устаревают.
"""
import time
import math

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import config


class TestParametrize:
    """
    Класс с тестами. Упавшие тесты собирают секретное сообщение.

    :cvar messages: список для сбора секретного сообщения.
    """

    messages: list = []

    @pytest.mark.parametrize("module", [
        "236895", "236896", "236897", "236898",
        "236899", "236903", "236904", "236905"
    ])
    def test_parametrize(self, browser: WebDriver, module: str) -> None:
        """Основные тест для множественного прогона и сбора секрета."""
        browser.get(f"https://stepik.org/lesson/{module}/step/1")

        WebDriverWait(browser, 15).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".navbar__auth_login")
        )).click()

        browser.find_element(By.ID, "id_login_email").send_keys(
            config.login_email.get_secret_value()
        )
        browser.find_element(By.ID, "id_login_password").send_keys(
            config.password.get_secret_value()
        )
        browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn").click()

        WebDriverWait(browser, 15).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".navbar__profile-img")
        ))

        textarea = WebDriverWait(browser, 15).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".ember-text-area"))
        )

        if not textarea.is_enabled():
            WebDriverWait(browser, 15).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button.again-btn")
            )).click()

        answer = math.log(int(time.time() + 2.0))
        text_area = WebDriverWait(browser, 15).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".ember-text-area")
        ))
        text_area.clear()
        text_area.send_keys(answer)

        WebDriverWait(browser, 15).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.submit-submission")
        )).click()

        correct = WebDriverWait(browser, 15).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".smart-hints__hint")
            )
        ).text

        try:
            assert correct == "Correct!", f"Тест {module} провален"
        except AssertionError:
            self.messages.append(correct.strip())
            raise

    @pytest.mark.parametrize("link", [
        "https://stepik.org/lesson/237240/step/5?unit=209628"
    ])
    def test_final(self, browser: WebDriver, link: str) -> None:
        """Этот тест выполнится один раз после всех параметризованных."""
        browser.get(link)
        full_message = " ".join(self.messages)

        WebDriverWait(browser, 15).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".navbar__auth_login")
        )).click()

        browser.find_element(By.ID, "id_login_email").send_keys(
            config.login_email.get_secret_value()
        )
        browser.find_element(By.ID, "id_login_password").send_keys(
            config.password.get_secret_value()
        )
        browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn").click()

        WebDriverWait(browser, 15).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".navbar__profile-img")
        ))

        WebDriverWait(browser, 15).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.button")
        )).click()

        textarea = WebDriverWait(browser, 15).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".ember-text-area"))
        )

        if not textarea.is_enabled():
            button = WebDriverWait(browser, 15).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "button.again-btn")
                )
            )
            browser.execute_script(
                "arguments[0].scrollIntoView(true);",
                button
            )
            button.click()

        text_area = WebDriverWait(browser, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".ember-text-area"))
        )
        text_area.clear()
        text_area.send_keys(full_message)

        WebDriverWait(browser, 15).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.submit-submission")
        )).click()

        correct = WebDriverWait(browser, 15).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".attempt-message_correct")
            )
        ).text
        print(f"correct={correct}")

        assert correct
