from base_page import BasePage

class DashboardPage(BasePage):

    def __init__(self):
        pass

    def greeting_link(self):
        return self.by_css('#wp-admin-bar-my-account .ab-item')
