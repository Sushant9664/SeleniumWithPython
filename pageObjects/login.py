

from selenium.webdriver.common.by import By

from Utils.browserutils import Browserutils
from pageObjects.shop import Shoppage


class LoginPage(Browserutils):
    #Constructor
    def __init__(self, driver):  #By sending as argument in the constructor driver is activated
        self.driver = driver
        super().__init__(driver)      #initalize util parent class driver
        self.Name = (By.CSS_SELECTOR, "input[name='name']")
        self.Emailid = (By.NAME, "email")
        self.Password = (By.ID, "exampleInputPassword1")
        self.Checkbox = (By.ID, "exampleCheck1")
        self.RadioButton = (By.CSS_SELECTOR, "#inlineRadio1")
        self.SubmitButton = (By.XPATH, "//input[@type='submit']")

    #Method
    def Login(self, name, emailid, password):
        self.driver.find_element(*self.Name).send_keys(name)   # * is sending two arguments as findelement need two arguements
        self.driver.find_element(*self.Emailid).send_keys(emailid)
        self.driver.find_element(*self.Password).send_keys(password)
        self.driver.find_element(*self.Checkbox).click()
        self.driver.find_element(*self.RadioButton).click()
        self.driver.find_element(*self.SubmitButton).click()
        shoppage = Shoppage(self.driver)
        return shoppage