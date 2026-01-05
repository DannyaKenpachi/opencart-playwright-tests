from pages.check_for_a_robot import CheckForARobot
from pages.main_page import MainPage
from pages.list_of_products import ListOfProducts
from pages.page_of_product import PageOfProduct
import pytest

@pytest.fixture
def check_for_a_robot(page):
    return CheckForARobot(page)

@pytest.fixture
def main_page(page):
    return MainPage(page)

@pytest.fixture
def list_of_products(page):
    return ListOfProducts(page)

@pytest.fixture
def page_of_product(page):
    return PageOfProduct(page)