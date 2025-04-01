import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.find_element(By.ID, "autocomplete").send_keys("Ind")
time.sleep(3)

countries= driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] div") #list[]
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break

# print(driver.find_element(By.ID, "autocomplete").text)
# updated dynamic value will not grab through hence use below method

print(driver.find_element(By.ID, "autocomplete").get_attribute("value"))
assert driver.find_element(By.ID, "autocomplete").get_attribute("value") == "India"
time.sleep(3)
