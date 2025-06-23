from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(
            *ProductPageLocators.BUTTON_ADD_TO_BASKET
        ).click()

    def name_validity_check(self):
        name = self.browser.find_element(
            *ProductPageLocators.NAME_PRODUCT
        ).text
        message_name = self.browser.find_element(
            *ProductPageLocators.MESSAGE_NAME_PRODUCT
        ).text
        assert (name == message_name,
                f"Не совпадает имя товара: {name} и {message_name}")

    def price_validity_check(self):
        price = self.browser.find_element(
            *ProductPageLocators.PRICE_PRODUCT
        ).text
        message_price = self.browser.find_element(
            *ProductPageLocators.MESSAGE_PRICE_PRODUCT
        ).text
        assert (price == message_price,
                f"Не совпадает цена товара: {price} и {message_price}")

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Success message is presented, but should not be"

    def should_disappeared(self):
        assert (self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE),
                "Success message is presented, but should not be")
