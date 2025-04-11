

from selenium.webdriver.common.by import By
from pageObjects.checkout_confirmation import Checkout_confirmation


class Shoppage:

    def __init__(self, driver):
        self.driver = driver
        self.shoplink = (By.CSS_SELECTOR, " a[href*='shop']")
        self.productname = (By.XPATH, "//div[@class='card h-100']")
        self.checkoputbutton = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def add_product_to_cart(self, Product):
        self.driver.find_element(*self.shoplink).click()
        products = self.driver.find_elements(*self.productname)
        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == "Product":
                product.find_element(By.XPATH, "div/button").click()

    def Go_to_cart(self):
        self.driver.find_element(*self.checkoputbutton).click()
        checkout_confirmation = Checkout_confirmation(self.driver)
        return checkout_confirmation
