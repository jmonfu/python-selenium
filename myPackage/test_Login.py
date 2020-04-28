import pytest

@pytest.yield_fixture
def setup():
    print("Open URL to loging")
    yield
    print("Close brower window after login")

def test_LoginByEmail(setup):  # we have to pass the testFixture ("setup") for it to run before
    print("this is login by Email")


def test_LoginByFacebook(setup):  # we have to pass the testFixture ("setup") for it to run before
    print("this is login by Facebook")
