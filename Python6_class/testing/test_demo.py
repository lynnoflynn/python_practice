import pytest


def test_a():
    print("test_demo.py 测试用例a")
def test_b():
    print("test_demo.py 测试用例b")
def test_c():
    assert 1==2
#生成3 X 3 =9 种测试用例
@pytest.mark.parametrize("a",[1,2,3])
@pytest.mark.parametrize("b",[4,5,6])
def test_param(a,b):
    print(f"a={a}, b={b}")