from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_product_in_basket(self):
        """Проверяет, что в корзине нет товаров"""
        assert self.is_element_present(
            *BasketPageLocators.PRODUCT_IN_BASKET
        ), "Корзина не пуста!"

    def should_be_empty_basket_message(self):
        """Проверяет, что отображается сообщение о пустой корзине"""
        assert self.is_element_present(
            *BasketPageLocators.MESSAGE_IN_BASKET
        ), "Сообщение о пустой корзине отсутствует!"
