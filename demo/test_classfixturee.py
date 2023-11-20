import pytest


@pytest.fixture(scope="class")
def login():
    print("this is login")
    yield
    print("this after")

@pytest.mark.usefixtures("login")
class TestDemo:
    def test_case1(self):
        print("this is testcaes1")
    def test_case2(self):
        print("this is testcaes2")