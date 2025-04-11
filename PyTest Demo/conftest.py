import pytest

#Fixtures is use for Set up and Tear down methods for test cases
#In conftest file if you declare any fixture that fixture will be available to all test file, test cases, methods that available in specific folder
#if you want to add fixture at class level just add scope = "Class" so it will run at the start and at the end only

# Set Up and Tear Down Methods
@pytest.fixture(scope="class")
def setup():
    print("I will print first")
    yield                           # Tear down from here
    print("I will print at last")

@pytest.fixture()
def dataload():
    print("Create My Data")
    return ["Sushant", "Waykar", "sushantwaykar@gmail.com"]  #using returm we can passed the data to test

#Fixture Parameterization
@pytest.fixture(params=["Chrome", "Firefox"])
def crossbrowser(request):
    return request.param