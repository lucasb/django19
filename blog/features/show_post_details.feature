Feature: Show post details
    As a standard user
    I want see a post details
    So that I can see whole post information

    Background: There are posts in blog
        Given there is a user:
            | id | username |
            | 1  | admin    |
        And there are a number of posts:
            |  id  |  title  |     text    |  author |
            |  1   | title 1 | post text 1 |  admin  |
            |  2   | title 2 | post text 2 |  admin  |
            |  3   | title 3 | post text 3 |  admin  |

    Scenario Outline: Show post details
        Given I am not logged user
        When I looking for post details from "<id>"
        Then I see this title "<title>"

        Examples:
            |    id   |  title    |
            |    1    |  title 1  |
            |    3    |  title 3  |
