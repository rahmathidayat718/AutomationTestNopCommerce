import pytest
from pytest_metadata.plugin import metadata_key
from selenium.webdriver.chrome import webdriver
from selenium import webdriver


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    return driver

# Format html-report
def pytest_configure(config):
    config.stash[metadata_key] ['Project Name'] = 'nopCommers'
    config.stash[metadata_key] ['Test Modul Name'] = 'Login User'
    config.stash[metadata_key] ['Tester Name'] = 'Rahmat Hidayat'
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)

########### INI UNTUK BEBERAPA BROWSER ###############
# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="chrome", help="Specify the browser: chrome or firefox or edge")
#
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")
# @pytest.fixture()
# def setup(browser):
#     global driver
#     if browser == "edge":
#         driver = webdriver.Edge()
#     elif browser == "chrome":
#         driver = webdriver.Chrome()
#     elif browser == "firefox":
#         driver = webdriver.Firefox()
#     else:
#         raise ValueError("Unsupported browser")
#     return driver