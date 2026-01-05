from playwright.sync_api import Page, expect

class PageOfProduct():
    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart = page.get_by_role('button', name='ADD TO CART')
        self.success_bar = page.locator('.bar-notification success')
        self.close_button_of_success_bar = page.get_by_title('Close')
    
    def add_product_to_cart(self):
        self.add_product_to_cart.click()
        expect(self.success_bar).to_be_visible()

    def close_success_message(self):
        self.close_button_of_success_bar.click()