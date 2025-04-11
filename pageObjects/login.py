

from selenium.webdriver.common.by import By
from pageObjects.shop import Shoppage


class LoginPage:
    #Constructor
    def __init__(self, driver):  #By sending as arugument in the constructor driver is activated
        self.driver = driver
        self.Name = (By.CSS_SELECTOR, "input[name='name']")
        self.Emailid = (By.NAME, "email")
        self.Password = (By.ID, "exampleInputPassword1")
        self.Checkbox = (By.ID, "exampleCheck1")
        self.RadioButton = (By.CSS_SELECTOR, "#inlineRadio1")
        self.SubmitButton = (By.XPATH, "//input[@type='submit']")

    #Method
    def Login(self):
        self.driver.find_element(*self.Name).send_keys("Sushant")   # * is sending two arguments as findelement need two arguements
        self.driver.find_element(*self.Emailid).send_keys("sushant.w@amazatic.com")
        self.driver.find_element(*self.Password).send_keys("Test@12345")
        self.driver.find_element(*self.Checkbox).click()
        self.driver.find_element(*self.RadioButton).click()
        self.driver.find_element(*self.SubmitButton).click()
        shoppage = Shoppage(self.driver)
        return shoppage