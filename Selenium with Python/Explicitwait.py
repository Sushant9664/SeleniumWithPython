import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
driver.implicitly_wait(5)  #Golbal Timeout

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")
time.sleep(3)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div") #list[]
count = len(results)
print(len(results))
assert count > 0

for result in results:
    result.find_element(By.XPATH, "div/button").click()   #chaining

driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, "//button[text()='Apply']").click()

Wait = WebDriverWait(driver, 10)  #given Explicitwait for the sepcific element
# Wait.until(expected_conditions.presence_of_element_located(By.CSS_SELECTOR, ".promoInfo"))
Wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
SuccessMessage = driver.find_element(By.CSS_SELECTOR, ".promoInfo").text
print(SuccessMessage)
assert "Code applied" in SuccessMessage






