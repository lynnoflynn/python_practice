import pytest

@pytest.fixture(scope="module")
def connectDB():
    print("connect db")
    yield
    print("disconnect")

#connectDB 这个参数至少要被传递一次才能被调用，一次都不用的话会被认为不需要这个fixture
#fixture生效的地点在参数开始传递的地点
def test_w():
    print("testcase_w")

class TestDemo1():
    def test_case1(self):
        print("testcase1")
    def test_case2(self):
        print("testcase2")
class TestDemo2():
    def test_case1(self,connectDB):
        print("testcase1")
    def test_case2(self):
        print("testcase2")