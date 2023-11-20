import pytest


@pytest.fixture(scope="function")
def login():
    print("this is login")

@pytest.mark.usefixtures("login")
def test_case1():
    print("this is testcaes1")


def test_case2():
    print("this is testcaes2")