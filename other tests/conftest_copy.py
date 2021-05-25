import pytest
from selenium import webdriver
import time

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="es",
                     help="Choose language: es ")


@pytest.fixture(scope="function")
def browser(request):
    user_lan = request.config.getoption("language")
    browser = None
    if user_lan == "es":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    else:
        raise pytest.UsageError("--language should be es")
    yield browser
    print("\nquit browser..")
    browser.quit()