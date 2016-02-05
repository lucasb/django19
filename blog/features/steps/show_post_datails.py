from behave import *

from blog.factories import PostFactory, UserFactory
from django.contrib.auth.models import User


# Copy the snippets from .feature into our file
@given('there is a user')
def backgrond(context):
    row = context.table[0]
    user = UserFactory(id=row['id'], username=row['username'])


@given('there are a number of posts')
def backgrond(context):
    posts = []
    for row in context.table:
        user = User.objects.filter(username=row['author']).first()
        posts.append(PostFactory(id=row['id'],
                                 title=row['title'],
                                 text=row['text'],
                                 author=user))


@given('I am not logged user')
def not_logged_user(context):
    context.browser.visit(context.config.server_url)


@when('I looking for post details from "{id}"')
def looking_post_details(context, id):
    url = '%s/post/%s' % (context.config.server_url, id)
    context.browser.visit(url)


@then('I see this title "{title}"')
def see_title(context, title):
    # command to see webpage that was redered.
    # context.browser.driver.save_screenshot('text.png')
    title_found = context.browser.find_by_css('.post h1').first.text
    assert title == title_found
