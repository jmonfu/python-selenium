import pytest

@pytest.yield_fixture
def setup():
    print("Open URL to Signup")
    yield
    print("Close brower window after singup")

def test_SignUpByEmail(setup):  # we have to pass the testFixture ("setup") for it to run before
    print("this is sign up by Email")


def test_SignUpByFacebook(setup):  # we have to pass the testFixture ("setup") for it to run before
    print("this is sign up by Facebook")
