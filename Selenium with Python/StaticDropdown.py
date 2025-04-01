import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

# Select class for the static dropdowns
staticdropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
staticdropdown.select_by_visible_text("Female")
# staticdropdown.select_by_index(0)
# staticdropdown.select_by_value()

time.sleep(3)



