import pytest
# import yaml

class TestCalc:
    @pytest.mark.add
    # @pytest.mark.parametrize("a,b,expect",adddatas,ids=myid)
    #有fixture拿数据 就不需要参数化了 在这里传入那个fixture (get_datas)就可以了
    def test_add1(self,get_calc,get_datas):
        result = get_calc.add(get_datas[0],get_datas[1])
        if isinstance(result,float):
            result = round(result,2)
        assert get_datas[2] == result