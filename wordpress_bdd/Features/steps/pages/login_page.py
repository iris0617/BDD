from base_page import BasePage
from dashboard_page import DashboardPage


class LoginPage(BasePage):

    def username(self):
        return self.by_id('username_id')


    def password(self):
        return self.by_id('')


    def submit_button(self):
        return self.by_id('wp-submit')


    def error_message(self):
        return self.by_id('error-msg').text.strip()

    def user_login(self, my_username, my_password):
        self.username().send_keys(my_username)
        self.password().send_keys(my_password)
        self.submit_button().click()
        return DashboardPage(self.driver)

    def clear_and_user_login(self, username, password):
        self.username().clear()
        self.user_login(username, password)


