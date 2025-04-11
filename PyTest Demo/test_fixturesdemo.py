from symtable import Class

import pytest
@pytest.mark.usefixtures("setup")
class Testexample:
    def test_fixturesdemo1(self):
        print("I will print at next step1")

    def test_fixturesdemo2(self):
        print("I will print at next step2")

    def test_fixturesdemo3(self):
        print("I will print at next step3")

    def test_fixturesdemo4(self):
        print("I will print at next step4")