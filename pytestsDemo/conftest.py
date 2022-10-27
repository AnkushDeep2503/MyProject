import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield  # it runs at the last for tear down method
    print("I will be executed last")


@pytest.fixture()
def dataLoad():
    print("User profile data is being created")
    return ["Rahul", "Shetty", "rahulshettyacademy.com"]


@pytest.fixture(params=[("Chrome", "Rahul", "Shetty"), ("Firefox", "Shetty"), ("IE", "SS")])
def crossBrowser(request):
    return request.param
