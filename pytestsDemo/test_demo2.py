# Test case name is Method name in pytest
import pytest


@pytest.mark.smoke
# @pytest.mark.skip
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test Failed"


def test_SecondCreditCard():
    a = 4
    b = 6
    assert a + 2 == 6, "Addition do not match"



