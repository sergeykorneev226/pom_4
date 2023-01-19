from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_basket.click()
        self.solve_quiz_and_get_code()

    def check_name_product_in_basket(self):
        product_message = self.browser.find_element(*ProductPageLocators.CHECK_NAME_PRODUCT)
        product_name = product_message.text
        assert "The shellcoder's handbook" in product_name, "Product's name is not correct"
        print("Added correct product")

    def check_price_basket_and_product(self):
        big_basket = self.browser.find_element(*ProductPageLocators.CHECK_PRICE_BIG_BASKET)
        big_basket_price = big_basket.text
        print(big_basket_price)
        mini_basket = self.browser.find_element(*ProductPageLocators.CHECK_PRICE_MINI_BASKET)
        mini_basket_price = mini_basket.text.partition(': ')[2]
        print(mini_basket_price)
        assert big_basket_price == mini_basket_price, "Product's price is not correct"
        print("Added correct product's price")
