from playwright.sync_api import Page

class CheckForARobot():
    def __init__(self, page: Page):
        self.page = page
        self.checkbox_for_robot = page.get_by_role('checkbox', name='Подтвердите, что вы человек')

    def checkbox_accept(self):
        if self.checkbox_for_robot.is_visible() and not self.checkbox_for_robot.is_checked():
            self.checkbox_for_robot.check()