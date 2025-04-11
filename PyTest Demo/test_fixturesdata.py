import pytest

@pytest.mark.usefixtures("dataload")
class Testexample2:

    def test_addmyprofile(self,dataload):   #to return data form fixture we have to pass the argument as fixturename
        print(dataload)
        print(dataload[0])  #retrive data as per indexing
        print(dataload[1])