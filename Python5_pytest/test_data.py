import pytest
import yaml

#ymal加载数据 yaml.safe_load yaml型数据里面-与数字之间记得留空格！！！
class TestData:
    @pytest.mark.parametrize(("a","b"),yaml.safe_load(open("./data.yaml")))
    def test_data(self,a,b):
        print(a+b)