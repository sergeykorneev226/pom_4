import time

from .pages.product_page import ProductPage


link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"


class TestProductPage():
    def test_guest_can_add_product_to_basket(self, browser):
        product = ProductPage(browser, link)
        product.open()
        product.add_product_to_basket()
        product.check_name_product_in_basket()
        product.check_price_basket_and_product()
        # time.sleep(60)

