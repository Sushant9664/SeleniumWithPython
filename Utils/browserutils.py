#when you have common code which is common for all Page object files then we can create one reusable utility file and declare all the methos
#make sure we can make this reusable util class as a parent to all your page object class
#intitalize driver with super class in PO files constructor

class Browserutils:

    def __init__(self, driver):
        self.driver = driver

    def getTitle(self):
        return self.driver.title