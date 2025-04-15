import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = None

#register option
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )

#run on diff browsers
@pytest.fixture(scope="function")
def browserinstance(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    # service_obj = Service()
    # if browser_name == "chrome":  # firefox
    #     driver = webdriver.Chrome(service=service_obj)
    # elif browser_name == "firefox":
    #     driver = webdriver.Firefox(service=service_obj)


    driver.implicitly_wait(4)
    request.node._driver = driver
    yield driver
    driver.close()

# #to capture failed screenshots
# @pytest.hookimpl( hookwrapper=True )
# def pytest_runtest_makereport(item):
#     """
#         Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
#         :param item:
#         """
#     pytest_html = item.config.pluginmanager.getplugin( 'html' )
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr( report, 'extra', [] )
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr( report, 'wasxfail' )
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             reports_dir = os.path.join( os.path.dirname( __file__ ), 'reports' )
#             file_name = os.path.join( reports_dir, report.nodeid.replace( "::", "_" ) + ".png" )
#             print( "file name is " + file_name )
#             _capture_screenshot( file_name )
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
#                 extra.append( pytest_html.extras.html( html ) )
#         report.extras = extra
#
# def _capture_screenshot(file_name):
#     driver.get_screenshot_as_file(file_name)

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             # Get the driver if it exists
#             driver = getattr(item, "_driver", None)
#             if driver is not None:
#                 # Create reports directory if it doesn't exist
#                 reports_dir = os.path.join(os.path.dirname(__file__), 'reports')
#                 os.makedirs(reports_dir, exist_ok=True)
#
#                 # Create a safe filename
#                 filename = report.nodeid.replace("::", "_")
#                 filename = "".join([c if c.isalnum() or c in ('_', '-', '.') else '_' for c in filename])
#                 file_path = os.path.join(reports_dir, filename + ".png")
#
#                 try:
#                     driver.get_screenshot_as_file(file_path)
#                     print(f"Screenshot saved to: {file_path}")
#
#                     if os.path.exists(file_path):
#                         html = f'<div><img src="{file_path}" alt="screenshot" style="width:600px;" onclick="window.open(this.src)" align="right"/></div>'
#                         extra.append(pytest_html.extras.html(html))
#                 except Exception as e:
#                     print(f"Failed to capture screenshot: {e}")
#
#         report.extras = extra
