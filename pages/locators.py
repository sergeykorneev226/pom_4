from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    CHECK_MESSAGE_NAME = (By.XPATH, "/html/body/div[2]/div/div[1]/div[1]/div/strong")
    CHECK_PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main > h1")
    CHECK_PRICE_MINI_BASKET = (By.CSS_SELECTOR, "div.basket-mini")
    CHECK_PRICE_BASKET = (By.CSS_SELECTOR, "p.price_color")
