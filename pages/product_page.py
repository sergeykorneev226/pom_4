import re
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_basket.click()
        self.solve_quiz_and_get_code()

    def check_name_product_in_basket(self):
        product_message = self.browser.find_element(*ProductPageLocators.CHECK_MESSAGE_NAME)
        product_message_text = product_message.text
        product_name = self.browser.find_element(*ProductPageLocators.CHECK_PRODUCT_NAME)
        product_name_text = product_name.text
        assert product_name_text == product_message_text, "Product's name is not correct"
        print("Product's name is correct")

    def check_price_basket_and_product(self):
        basket = self.browser.find_element(*ProductPageLocators.CHECK_PRICE_BASKET)
        basket_text = basket.text
        basket_price = re.findall('\d+', basket_text)
        mini_basket = self.browser.find_element(*ProductPageLocators.CHECK_PRICE_MINI_BASKET)
        mini_basket_text = mini_basket.text
        mini_basket_price = re.findall('\d+', mini_basket_text)
        assert basket_price == mini_basket_price, "Product's price is not correct"
        print("Product's price is correct")
