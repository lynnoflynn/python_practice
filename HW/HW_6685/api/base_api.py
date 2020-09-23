import requests
from jsonpath import jsonpath

# base_api 完成最基本的封装
class BaseApi():
    # 定义requests(字典格式需要用**解包)
    def base_send_requests(self,req:dict):
        return requests.request(**req)

    # 定义json path
    def base_json_path(self,obj,json_exp):
        return jsonpath(obj,json_exp)
