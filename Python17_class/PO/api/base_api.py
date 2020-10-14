import requests
from jsonpath import jsonpath
from jsonschema import validate


class BaseApi:
    def send_requests(self,req:dict):
        #对requests 进行二次分装
        # req = {
        #     "method" : "get",
        #     "url": "xxx",
        #     "params": {},
        #     "json": {},
        # }
        #等同于requests.request(method=get, url="xxx",params={},json={})
        return requests.request(**req)

    def base_jsonpath(self,obj,json_expr):
        return jsonpath(obj,json_expr)

    def base_jsonschema(self,instance,schema):
        return validate(instance,schema)