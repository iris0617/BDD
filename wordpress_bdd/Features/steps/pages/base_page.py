from selenium import webdriver

class BasePage(object):

    url = None
    driver = None
    domain = None

    def __init__(self, driver):
        self.driver = driver
        self.domain = 'http://localhost/wordpress'

    def title(self):
        return self.driver.get_title()

    def get_current_url(self):
        return self.driver.current_url

    def navigate(self, url):
        self.driver.get(url)

    def by_id(self, id):
        return self.driver.find_element_by_id(id)

    def by_name(self, name):
        return self.driver.find_element_by_name(name)

    def by_css(self, css):
        return self.driver.find_element_by_css_selector(css)

    def js(self,js):
        self.driver.execute_script(js)

    def fill_form_by_css(self, css, value):
        self.driver.find_element_by_css_selector(css).send_keys(value)

    def fill_form_by_id(self, id, value):
        self.driver.find_element_by_css_selector(id).send_keys(value)