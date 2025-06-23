import pytest

from pages.product_page import ProductPage


@pytest.mark.parametrize('promo', ["newYear2019", "offer0", "offer1",
                                   "offer2", "offer3", "offer4", "offer5",
                                   "offer6", "offer7", "offer8", "offer9"])
def test_guest_can_add_product_to_basket(browser, promo):
    page = ProductPage(
        browser,
        f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={promo}"
    )
    page.open()
    page.should_not_be_success_message()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.name_validity_check()
    page.price_validity_check()
    page.should_disappeared()


def test_guest_cant_see_success_message_after_adding_product_to_basket(
        browser):
    page = ProductPage(
        browser,
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    )
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(
        browser,
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    )
    page.open()
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(
        browser,
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    )
    page.open()
    page.add_to_basket()
    page.should_disappeared()
