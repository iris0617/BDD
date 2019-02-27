Feature: create_post
@create_post
Scenario: success
    When cp post with title and content
        Then cp display new post title
