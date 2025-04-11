import pytest
from selenium import webdriver

#register option
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )

#run on diff browsers
@pytest.fixture(scope="function")
def browserinstance(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    if browser_name == "firefox":
        driver = webdriver.Firefox()

    driver.implicitly_wait(4)
    yield driver
    driver.close()
