import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

## Chrome Headless mode
Chrome_options = webdriver.ChromeOptions()
#Chrome_options.add_argument("headless")
Chrome_options.add_argument("--ignore-certificates-error")  ##Ignore ssl certificates
Chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=Chrome_options)
driver.implicitly_wait(5)  #Golbal Timeout

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.title)

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")  ##How to scroll on webpage
driver.get_screenshot_as_file("Screenshot.png")   ##How to take screenshots
time.sleep(3)