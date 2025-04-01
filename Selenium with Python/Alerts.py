# Browser, Java, Java Scripts Alerts
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
Name = "Sushant"
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "#name").send_keys(Name)
driver.find_element(By.ID, "alertbtn").click()
alerts = driver.switch_to.alert   # method to handled or switched on alert
TextonAlert = alerts.text
print(TextonAlert)
assert Name in TextonAlert
alerts.accept()                   # Method to click on Ok or any accept buttoon which is on alert
# alerts.dismiss()                  # Method to click on Cancel or any reject buttoon which is on alert


time.sleep(3)