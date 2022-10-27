import pytest


@pytest.mark.smoke
def test_firstProgram(setup):
    print("anything")


@pytest.mark.xfail
def test_secondProgram():
    a = 3
    b = 4
    assert a == b


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])