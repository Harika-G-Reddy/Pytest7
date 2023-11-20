import pytest


@pytest.fixture()
def setup():
    print("this is setup")
    yield
    print("this is after")

def test_case1(setup):
    print("this is testcaes1")


def test_case2(setup):
    print("this is testcaes2")