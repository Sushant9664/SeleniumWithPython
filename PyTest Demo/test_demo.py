import pytest


@pytest.mark.smoke
def test_firstprogram(setup):
    print("Hello")

@pytest.mark.xfail
def test_creditcard():
    print("Good Morning")

def test_crossbrowsertesting(crossbrowser):
    print(crossbrowser)