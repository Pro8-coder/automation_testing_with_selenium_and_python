"""
Ваша задача -- реализовать автотест со следующим набором действий:

открыть в Chrome урок по ссылке https://stepik.org/lesson/236895/step/1
авторизоваться со своими логином и паролем
дождаться того, что поп-апа с авторизацией больше нет
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import config


link = "https://stepik.org/lesson/236895/step/1"


class TestParametrize:
    def test_parametrize(self, browser):
        browser.get(link)

        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.ID, "ember479"))
        ).click()

        browser.find_element(By.ID, "id_login_email").send_keys(
            config.login_email.get_secret_value()
        )
        browser.find_element(By.ID, "id_login_password").send_keys(
            config.password.get_secret_value()
        )
        browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn").click()

        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "img.navbar__profile-img")
            )
        )
