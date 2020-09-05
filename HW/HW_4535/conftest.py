from urllib import request

import pytest
import yaml
from Python7_class.calc import Calculator


#用fixture class setup，设置范围级别为类
@pytest.fixture(scope="class")
def get_calc():
    print("获取计算机实例")
    calc = Calculator()
    return calc

#用fixture导入数据 加减乘除的数据和数据类型
with open ("./calc.yml") as f:
    data = yaml.safe_load(f)["data"]
    add_data = data["add_data"]
    add_datatype = data["add_datatype"]
    sub_data = data["sub_data"]
    sub_datatype = data["sub_datatype"]
    mul_data = data["mul_data"]
    mul_datatype = data["mul_datatype"]
    div_data = data["div_data"]
    div_datatype = data["div_datatype"]
@pytest.fixture(params=add_data,ids=add_datatype)
def get_data1(request):
    print("开始加法运算")
    result = request.param
    print(f"计算结果是{result}")
    yield result
    print ("结束加法运算")
@pytest.fixture(params=sub_data,ids=sub_datatype)
def get_data2(request):
    print("开始减法运算")
    result = request.param
    print(f"计算结果是{result}")
    yield result
    print ("结束减法运算")
@pytest.fixture(params=mul_data,ids=mul_datatype)
def get_data3(request):
    print("开始乘法运算")
    result = request.param
    print(f"计算结果是{result}")
    yield result
    print ("结束乘法运算")
@pytest.fixture(params=div_data,ids=div_datatype)
def get_data4(request):
    print("开始除法运算")
    result = request.param
    print(f"计算结果是{result}")
    yield result
    print ("结束除法运算")
