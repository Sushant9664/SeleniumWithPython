import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)  #Golbal Timeout
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.switch_to.frame("courses-iframe") #switch to frame
driver.find_element(By.XPATH, "(//a[text()='JOIN NOW']) [1]").click()

driver.switch_to.default_content()  #switch back to main page
driver.find_element(By.XPATH, "//input[@value='radio1']").click()

time.sleep(3)