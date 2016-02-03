from behave import *

from splinter.browser import Browser

from django.core import management


def before_all(context):
    if context.config.browser:
        context.browser = Browser(context.config.browser)
    else:
        context.browser = Browser('phantomjs')

    # When we're running with PhantomJS we need to specify the window size.
    # This is a workaround for an issue where PhantomJS cannot find elements
    # by text - see: https://github.com/angular/protractor/issues/585
    if context.browser.driver_name == 'PhantomJS':
        context.browser.driver.set_window_size(1280, 1024)

def before_scenario(context, scenario):
    # Reset the database before each scenario.
    management.call_command('flush', verbosity=0, interactive=False)

def after_all(context):
    # Quit browser when all test is done.
    context.browser.quit()
    context.browser = None
