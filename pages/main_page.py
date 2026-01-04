from playwright.sync_api import Page

class MainPage():
    def __init__(self, page: Page):
        self.page = page
        self.search_field = page.get_by_role("textbox", name="Search store")
        self.button_search = page.get_by_role("button", name="Search")
    
    def search_product(self):
        self.search_field.click()
        self.search_field.fill("MacBook")
        self.button_search.click()

