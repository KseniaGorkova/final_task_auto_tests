from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import pytest
from selenium import webdriver
import pytest
import time



@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?plromo=offer0",
                                 pytest.param("ttp://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?plromo", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?plromo=offer0"],
                                 )
def test_guest_can_add_product_to_basket(browser,link):
    
    basket_page = ProductPage(browser,link)
    basket_page.open()
    basket_page.should_be_basket()
    