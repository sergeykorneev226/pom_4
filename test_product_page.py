import pytest
from .pages.product_page import ProductPage


link_1 = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link_2 = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
link_3 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


class TestProductPage():
    # def test_guest_can_add_product_to_basket(self, browser):
    #     product = ProductPage(browser, link_2)
    #     product.open()
    #     product.add_product_to_basket()
    #     product.check_name_product_in_basket()
    #     product.check_price_basket_and_product()
        # time.sleep(60)

    # @pytest.mark.xfail
    # @pytest.mark.parametrize('link',
    #                          ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    #                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    #                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    #                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    #                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    #                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    #                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    #                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
    #                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    #                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
    # def test_promo_guest_can_add_product_to_basket(self, browser, link):
    #     product = ProductPage(browser, link)
    #     product.open()
    #     product.add_product_to_basket()
    #     product.check_name_product_in_basket()
    #     product.check_price_basket_and_product()
        # time.sleep(60)

    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        product = ProductPage(browser, link_3)
        product.open()
        product.add_product_to_basket()
        product.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        product = ProductPage(browser, link_3)
        product.open()
        product.should_not_be_success_message()

    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        product = ProductPage(browser, link_3)
        product.open()
        product.add_product_to_basket()
        product.should_be_disappear()


    # def test_guest_should_see_login_link_on_product_page(self, browser):
    #     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    #     page = ProductPage(browser, link)
    #     page.open()
    #     page.should_be_login_link()
    #
    # def test_guest_can_go_to_login_page_from_product_page(self, browser):
    #     pass
