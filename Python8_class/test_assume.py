import pytest


def test_a():
    #这样一旦成功后面的就不运行了
    # assert 1==1
    # assert False==True
    # assert 200==100

    #用pytest.assume这样就算第一个成功后面的也会执行
    pytest.assume(1==1)
    pytest.assume(False==True)
    pytest.assume(200==100)
