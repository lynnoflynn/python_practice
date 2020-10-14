import pytest

#创建一个登录的fixture方法
#fixture 是Pytest的外壳函数，可以莫伊setup，teardown 操作
#yield关键字激活了fixture的teardown方法
#yield之前的操作相当于setup，之后的操作相当于teardown
#yield相当于return，若想要返回一些测试数据，可以放在yield后面返回到测试用例中
#autouse是自动使用,则不需要在测试用例括号里传入 login了
@pytest.fixture(autouse=True)
def login():
    print("登录操作")
    print("获取token")
    username = "tom"
    password = "123456"
    token = "12315641654"
    # return [username,password,token]
    #yield激活teardown操作
    yield [username,password,token]
    print("登出操作")

#测试用例1：需要提前登录,就把名字传入进去
#在执行测试用例之前会执行【传入的】fixture方法
def test_case1(login):
    print(f"login username and password: {login}")
    print("testcase1")
#测试用例2：不需要提前登录
def test_case2(connectDB):
    print("testcase2")
#测试用例3：需要提前登录
def test_case3(login):
    print("testcase3")
