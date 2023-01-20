import re
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_basket.click()
        # self.solve_quiz_and_get_code()

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

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.CHECK_MESSAGE_NAME), "Success message is presented, but should not be"

    def should_be_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.CHECK_MESSAGE_NAME), "Element is not disappeared, but should be"





    # @pytest.mark.login
    # class TestLoginFromProductPage():
    #     @pytest.fixture(scope="function", autouse=True)
    #     def setup(self):
    #         self.product = ProductFactory(title="Best book created by robot")
    #         # создаем по апи
    #         self.link = self.product.link
    #         yield
    #         # после этого ключевого слова начинается teardown
    #         # выполнится после каждого теста в классе
    #         # удаляем те данные, которые мы создали
    #         self.product.delete()
    #
    #     def test_guest_can_go_to_login_page_from_product_page(self, browser):
    #         page = ProductPage(browser, self.link)
    #         # дальше обычная реализация теста
    #
    #     def test_guest_should_see_login_link(self, browser):
    #         page = ProductPage(browser, self.link)
    #         # дальше обычная реализация теста

