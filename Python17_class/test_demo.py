import requests
from hamcrest import assert_that, equal_to
from jsonpath import jsonpath
import hamcrest

class TestDemo():
    def test_get(self):
        r = requests.get('http://httpbin.testing-studio.com/get')
        # print(r.status_code)
        print(r.text)
        # print(r.json())
        assert r.status_code  == 200
    #get query请求
    def test_query(self):
        payload={
            "level":1,
            "name":"lynnaaa"
        }
        r = requests.get('http://httpbin.testing-studio.com/get',params=payload)
        print(r.text)
        assert r.status_code == 200
    #form 请求参数构造
    def test_post_form(self):
        payload = {
            "level": 1,
            "name": "lynnaaa"
        }
        r = requests.post('http://httpbin.testing-studio.com/post',data=payload)
        print(r.text)
        assert r.status_code == 200

    # header
    def test_post_header(self):
        r = requests.get('http://httpbin.testing-studio.com/get',headers={"h":"header demo"})
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code  == 200
        assert r.json()['headers']['H'] == "header demo"

    # post json
    def test_post_json(self):
        payload = {
            "level": 1,
            "name": "lynnaaa"
        }
        r = requests.post('http://httpbin.testing-studio.com/post', json=payload)
        print(r.text)
        assert r.status_code == 200
        assert r.json()['json']['level'] == 1
    #json断言

    def test_hogwarts_assert(self):
        r = requests.get('https://ceshiren.com/categories.json')
        print(r.text)
        assert r.status_code == 200
        # assert r.json()['category_list']['categories'][0['name'] == "社区治理"
        # 打印这个列表所有名字
        print(jsonpath(r.json(), '$..name'))
        #jsonpath断言
        assert jsonpath(r.json(),'$..name')[0] == "社区治理"

    def test_hamcrest(self):
        r = requests.get('https://ceshiren.com/categories.json')
        print(r.text)
        # jsonpath断言
        # assert jsonpath(r.json(), '$..name')[0] == "社区治理"
        #hamcrest 断言
        assert_that(jsonpath(r.json(), '$..name')[0], equal_to("社区治理"))






