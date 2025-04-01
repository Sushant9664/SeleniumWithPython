import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

radiobuttons = driver.find_elements(By.XPATH, "//input[@type='radio']")
print(len(radiobuttons))
radiobuttons[2].click()  #if indexing is fixed for the options use this method
assert radiobuttons[2].is_selected()

time.sleep(3)

for radiobutton in radiobuttons:
    if radiobutton.get_attribute("value") == "radio2":
        radiobutton.click()
        assert radiobutton.is_selected()
        break


assert driver.find_element(By.ID, "displayed-text").is_displayed() #to check element displayed on not
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed() #to check negative asserton

time.sleep(3)
