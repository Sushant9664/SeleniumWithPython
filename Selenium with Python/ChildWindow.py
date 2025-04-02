import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)  #Golbal Timeout
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.ID, "opentab").click()
windowswitch = driver.window_handles
driver.switch_to.window(windowswitch[1])  #switched to 2nd tab
driver.find_element(By.XPATH, "//a[text()='Access all our Courses']").click()

driver.switch_to.window(windowswitch[0]) #switched to 1st tab
driver.find_element(By.XPATH, "//input[@value='radio1']").click()

time.sleep(2)