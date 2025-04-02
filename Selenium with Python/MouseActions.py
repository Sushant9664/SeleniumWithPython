import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)  #Golbal Timeout
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

action = ActionChains(driver)   # to import mouse actions
# action.click_and_hold().perform()
# action.context_click().perform()
# action.double_click().perform()
# action.click_and_hold().perform()
# action.drag_and_drop().perform()
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform() #mouse hover
action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()  #right click
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()

