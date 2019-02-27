from base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class PostListPage(BasePage):

    def first_post(self):
        return self.by_id('.row-title')

    def delete_post(self, post_id):
        post_selector = 'post-' + post_id
        the_row = self.by_id(post_selector)
        ActionChains(self.driver).move_to_element(the_row).perform()
        the_row.find_element_by_css_selector('.submitdelete').click()


