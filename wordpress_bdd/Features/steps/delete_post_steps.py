from behave import *
import edit_post_page
import post_list_page



@When('dp post with {title} and {content} and return its id')
def step_impl(context, title, content):
    context.edit_post_page = edit_post_page.EditPostPage(context.dr)
    context.edit_post_page.url = 'http://localhost/wordpress/wp-admin/post-new.php'
    context.edit_post_page.navigate()
    context.edit_post_page.post_id = context.edit_post_page.create_post_and_return_its_id(title, content)
    context.title = title



@When('dp delete the new post')
def step_impl(context):
    context.post_list_page = post_list_page.PostListPage(context.dr)
    context.post_list_page.url = 'http://localhost/wordpress/wp-admin/edit.php'
    context.post_list_page.navigate()
    selected_post_id = context.edit_post_page.post_id
    context.post_list_page.delete_post_by_id(selected_post_id)


@Then('dp the new post should not be on post list page')
def step_impl(context, title):
    context.post_list_page.navigate()
    assert  context.post_list_page.first_post().text.strip() != context.title