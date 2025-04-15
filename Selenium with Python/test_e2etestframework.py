import json
import os
import sys

import pytest

sys.path.append( os.path.dirname( os.path.dirname( os.path.abspath( __file__ ) ) ) )
from pageObjects.shop import Shoppage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.login import LoginPage

# pytest -n 2 -m smoke --browser_name firefox --html=reports/report.html


#This will import data from the json file
test_data_path = '../Data/test_e2etestframework.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@pytest.mark.smoke
@pytest.mark.parametrize("test_item_list", test_list)      #to parametrize data
def test_e2e(browserinstance, test_item_list):
    driver = browserinstance
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    loginPage = LoginPage(driver)  #Initalize object for the LoginPage class
    print(loginPage.getTitle())
    shoppage = loginPage.Login(test_item_list["Name"], test_item_list["emailid"], test_item_list["password"] )        #Called Login method from login class
    shoppage.add_product_to_cart(test_item_list["Product"])
    print(shoppage.getTitle())
    checkout_confirmation = shoppage.Go_to_cart()
    checkout_confirmation.Checkout()
    checkout_confirmation.Address_page("ind")
    checkout_confirmation.Succes_Message()
