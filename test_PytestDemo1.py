import pytest

@pytest.fixture()
def setup():
    print("Once before every method")


def testMethod1(setup):  # we have to pass the testFixture ("setup") for it to run before
    print("this is test method 1")


def testMethod2(setup):  # we have to pass the testFixture ("setup") for it to run before
    print("this is test method 2")
