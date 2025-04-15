
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def test_sort(browserinstance):
    driver = browserinstance
    veggisoptions = []
    driver.implicitly_wait(5)  # Golbal Timeout
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    # click on column header
    driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

    # list down the veggies name
    veggilist = driver.find_elements(By.XPATH, "//tr/td[1]")
    for veggis in veggilist:
        veggisoptions.append(veggis.text)
    print(veggisoptions)
    Copyveggisinnewlist = veggisoptions.copy()  # This will create another copy of the list
    print(Copyveggisinnewlist)

    # sort using selenium method
    veggisoptions.sort()
    assert veggisoptions == Copyveggisinnewlist
