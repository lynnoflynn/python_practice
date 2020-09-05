import pytest
#定义测试类
class TestCalc():
    #装饰器标记加法
    @pytest.mark.add
    #fixture导入加法运算的数据
    def test_add(self,get_calc,get_data1):
        result = get_calc.add(get_data1[0],get_data1[1])
        if isinstance(result,float):
            result = round(result,2)
        assert get_data1[2] == result

    # fixture导入减法运算的数据
    @pytest.mark.sub
    def test_sub(self, get_calc, get_data2):
        result = get_calc.sub(get_data2[0], get_data2[1])
        if isinstance(result, float):
            result = round(result, 2)
        assert get_data2[2] == result

    # fixture导入乘法运算的数据
    @pytest.mark.mul
    def test_mul(self, get_calc, get_data3):
        result = get_calc.mul(get_data3[0], get_data3[1])
        if isinstance(result, float):
            result = round(result, 2)
        assert get_data3[2] == result

    # fixture导入除法运算的数据
    @pytest.mark.div
    def test_div(self, get_calc, get_data4):
        result = get_calc.div(get_data4[0], get_data4[1])
        if isinstance(result, float):
            result = round(result, 2)
        assert get_data4[2] == result
