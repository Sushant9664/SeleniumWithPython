import pytest


@pytest.mark.smoke
def test_firstprogram():
    messg = "Hello"
    assert messg == "Hi", "Messg doensont matched"

@pytest.mark.skip
def test_creditcard():
    a = 4
    b = 6
    assert a+2 == 6, "Addition matched"

