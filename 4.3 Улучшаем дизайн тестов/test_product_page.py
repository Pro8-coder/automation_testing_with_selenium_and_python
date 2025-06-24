import pytest

from pages.basket_page import BasketPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage


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


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(
        browser,
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    )
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_product_in_basket()
    basket_page.should_be_empty_basket_message()
