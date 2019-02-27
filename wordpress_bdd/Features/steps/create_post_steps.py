from behave import *
import edit_post_page
import post_list_page



@when('cp post with {title} and {content}')
def step_impl(context, title, content):
    context.create_post_page = edit_post_page.EditPostPage(context.dr)
    context.create_post_page.url = 'http://wordpress/wp-admin/post-new.php'
    context.create_post_page.navigate()
    context.create_post_page.create_post(title, content)
    context.title = title




@then('cp display new post {title}')
def step_impl(context, title):
    context.post_list_page = post_list_page.PostListPage(context.dr)
    context.post_list_page.url = 'http://wordpress/wp-admin/edit.php'
    context.post_list_page.navigate()
    assert context.title == context.post_list_page.first_post().text.strip()