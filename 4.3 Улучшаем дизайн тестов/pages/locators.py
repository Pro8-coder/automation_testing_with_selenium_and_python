from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    NAME_PRODUCT = (By.CSS_SELECTOR, '.product_main h1')
    PRICE_PRODUCT = (By.CSS_SELECTOR, '.product_main .price_color')
    MESSAGE_NAME_PRODUCT = (By.CSS_SELECTOR,
                            '#messages > :nth-child(1) strong')
    MESSAGE_PRICE_PRODUCT = (By.CSS_SELECTOR,
                             '#messages > :nth-child(3) strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div[id="messages"] div:first-child')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
