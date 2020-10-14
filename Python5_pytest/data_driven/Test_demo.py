import pytest
import yaml


class TestDemo:
    #参数化里面若是字典，则只会打印key值，所以一般要转化成列表list才能打印全
    @pytest.mark.parametrize("env",yaml.safe_load(open("./env.yml")))
    def test_demo(self,env):
        if "test" in env:
            print("这是测试环境")
            #env["key值"]
            print("测试环境的ip是:", env["test"])
        elif "dev" in env:
            print("这是开发环境")
            print("开发环境的ip是:", env["dev"])
