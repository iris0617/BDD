from base_page import BasePage

class EditPostPage(BasePage):

        def post_title(self):
            return self.by_id('title')

        def set_content(self, content):
            js = 'document.getElementById("content_ifr").contentWindow.document.body.innerHTML = "%s"' % content
            print(js)
            self.js(js)

        def publish_button(self):
            return self.by_id('publish')

        def permanent_link(self):
            return self.by_id('sample-permalink')

        def create_post(self, title, content):
            self.post_title().send_keys(title)
            self.set_content(content)
            self.publish_button().click()

        def create_post_and_return_its_id(self, title, content):
            self.create_post(title, content)
            link_arr = self.permanent_link().text.split('=')
            token = link_arr[-1]
            return token
