
#conftest可以覆盖到同级目录 其子目录
#fixture 读取顺序：
#当前文件->当前目录->上一级别目录
import pytest
import yaml

from Python7_class.calc import Calculator

@pytest.fixture(scope="session")
def connectDB():
    print("connect db")
    yield
    print("disconnect")

#可以返回想要的对象和测试数据
#可以通过灵活地控制作用域的范围来实现自动化的操作
@pytest.fixture(scope="class")
def get_calc():
    print("获取计算器实例")
    calc = Calculator()
    return calc

#用fixture 拿数据 和ID
#用request来获取参数

with open("./calc.yml") as f:
    datas = yaml.safe_load(f)["add"]
    adddatas = datas["datas"]
    myid = datas["myid"]

@pytest.fixture(params=adddatas, ids=myid)
def get_datas(request):
    print("开始计算")
    data = request.param
    print(f"request.param的测试数据是{data}")
    yield data
    print("结束计算")
