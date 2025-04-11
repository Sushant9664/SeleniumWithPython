import os
import sys

sys.path.append( os.path.dirname( os.path.dirname( os.path.abspath( __file__ ) ) ) )

from pageObjects.shop import Shoppage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.login import LoginPage


def test_e2e(browserinstance):
    driver = browserinstance
    driver.get("https://rahulshettyacademy.com/angularpractice/")

    loginPage = LoginPage(driver)  #Initalize object for the LoginPage class
    shoppage = loginPage.Login()        #Called Login method from login class
    shoppage.add_product_to_cart("Blackberry")
    checkout_confirmation = shoppage.Go_to_cart()
    checkout_confirmation.Checkout()
    checkout_confirmation.Address_page("ind")
    checkout_confirmation.Succes_Message()
