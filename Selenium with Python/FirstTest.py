import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# If vpn restrictions are there and webdriver not able to download the chrome driver
# service_obj= Service("C:/Users/User/AppData/Local/Programs/Python/Python39/Scripts/chromedriver.exe")
# browser = webdriver.Chrome(service=service_obj)

browser = webdriver.Chrome()
browser.get('https://selenium.dev/')
browser.maximize_window()
title = browser.title
print(title)
print(browser.current_url)

assert "Selenium" in title


time.sleep(3)