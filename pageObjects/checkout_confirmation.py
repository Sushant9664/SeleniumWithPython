
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Utils.browserutils import Browserutils


class Checkout_confirmation(Browserutils):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)  # initalize util parent class driver
        self.checkout_button = (By.XPATH, "//button[@class='btn btn-success']")
        self.country_input = (By.ID, "country")
        self.country_option = (By.LINK_TEXT, "India")
        self.checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.submitbutton = (By.CSS_SELECTOR, "[type='submit']")
        self.successtext = (By.CLASS_NAME, "alert-success")

    def Checkout(self):
        self.driver.find_element(*self.checkout_button).click()

    def Address_page(self, countryname):
        self.driver.find_element(*self.country_input).send_keys(countryname)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element(*self.country_option).click()
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.submitbutton).click()

    def Succes_Message(self):
        successText = self.driver.find_element(*self.successtext).text
        assert "Success! Thank you!" in successText
