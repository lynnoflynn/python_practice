import pytest
import yaml
# 引入计算器
from Python6_class.calc import Calculator
#yaml导入加和除的测试用例
with open("./calc.yml") as f:
    data = yaml.safe_load(f)["data"]
    add_data = data["add_data"]
    add_datatype = data["add_datatype"]
    div_data = data["div_data"]
    div_datatype = data["div_datatype"]


#定义测试类 继承自Calculator
class TestCalc():
    #测试类执行前的操作：setup_class()
    def setup_class(self):
        print("开始计算")
        #实例化计算器
        self.calc = Calculator()
    #测试后执行后的操作：teardown_cloass()
    def teardown_class(self):
        print("计算结束")
    #每次执行测试用例前的操作
    def setup(self):
        print("开始执行测试用例")
    #每次执行测试用例之后的操作
    def teardown(self):
        print("结束测试用例的执行")

    #装饰器标记所有加法运算
    @pytest.mark.add
    #使用参数化完成测试用例的自动生成
    @pytest.mark.parametrize("a,b,expect",add_data,ids=add_datatype)
    #调用计算器的加法运算方法
    def test_add(self,a,b,expect):
        result = self.calc.add(a,b)
        if isinstance(result,float):
         result = round(result,2)
        #断言
        assert expect == result

    #标记所有除法运算
    @pytest.mark.div
    @pytest.mark.parametrize("a,b,expect", div_data, ids=div_datatype)
    # 调用计算器的除法法运算方法
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        # 断言
        assert expect == result