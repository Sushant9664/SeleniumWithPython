import time


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
print(driver.title)

driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Sushant")
driver.find_element(By.NAME, "email").send_keys("sushant.w@amazatic.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Test@12345")
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()

Message = driver.find_element(By.CLASS_NAME, "alert-success").text  #to grab the text
print(Message)
assert "Success" in Message

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("sushantwaykar")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear() #to clear the text field





time.sleep(3)