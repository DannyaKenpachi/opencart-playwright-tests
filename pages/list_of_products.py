from playwright.sync_api import Page

class ListOfProducts():
    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart = page.get_by_role('button', name='ADD TO CART')
    
    def open_page_of_product(self):
        self.add_to_cart.click()