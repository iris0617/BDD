Feature: delete_post
@delete_post
Scenario:success
    When dp post with title and content and return its id
    When dp delete the new post
  Then dp the new post should not be on post list page
