import pytest

@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will be executed last")

@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Ardak", "Akishev", "www.ardaka.github.com.io/ardakakishev"]

@pytest.fixture(params=[("chrome","Ardak","Akishev"),("Firefox","Akishev"), ("IE","SS")])
def crossBrowser(request):
    return request.param

