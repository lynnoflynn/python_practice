#文件名以test_开头，类名以Test开头，方法名以test_开头
#测试类一定不要加__init__方法
import pytest
import yaml

from Python6_class.calc import Calculator

with open("calc.yml") as f:

    datas = yaml.safe_load(f)["add"]
    adddatas = datas["datas"]
    print(adddatas)
    myid = datas["myid"]
    print(myid)

class TestCalc:
    def setup_class(self):
        print("开始计算")
        # 实例化计算器
        self.calc = Calculator()
    def teardown_class(self):
        print("结束计算")
    @pytest.mark.add
    @pytest.mark.parametrize("a,b,expect",adddatas,ids=myid)
    def test_add(self,a,b,expect):
        # #实例化计算器
        # calc=Calculator()
        #调用它的相加add()方法
        result = self.calc.add(a,b)
        #断言（判定条件）
        #浮点数运算可能会出现的报错，解决办法：round(,)
        if isinstance(result,float):
            result = round(result,2)
        assert expect == result



    @pytest.mark.div
    def test_div(self):
        #实例化计算器
        # calc=Calculator()
        # #调用它的相加div()方法
        r = self.calc.div(1,1)
        #断言（判定条件）
        assert 1 == r

    @pytest.mark.div
    def test_div1(self):
        #实例化计算器
        # calc=Calculator()
        r = self.calc.div(-1,1)
        #断言（判定条件）
        assert -1 == r
