from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import MainPageLocators, LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        current_url = self.browser.current_url
        assert ("login" in current_url,
                f"Expected 'login' in URL, but got: {current_url}")

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert (self.is_element_present(*LoginPageLocators.LOGIN_FORM),
                "Login form is not present")

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert (self.is_element_present(*LoginPageLocators.REGISTER_FORM),
                "Register form is not present")
