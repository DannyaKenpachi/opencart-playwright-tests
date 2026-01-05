import pytest
import allure

def test_check_for_a_robot(check_for_a_robot):
    check_for_a_robot.checkbox_accept()
    check_for_a_robot.navigate()

def test_add_product_to_cart(main_page, list_of_products):
    main_page.search_product()
    list_of_products.open_page_of_product()

def close_success_bar(page_of_product):
    page_of_product.close_success_message()