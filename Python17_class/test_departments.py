import requests

class TestDepartments():
    def setup(self):
        """
        获取token
        """
        corpid = "wwa06955e5c907354a"
        corpsecret = "_8yRExPVFzRiQhR7amDTLbBky58dBZqu2DuuDj019IU"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        # 定义请求参数
        params = {
            "corpid": corpid,
            "corpsecret": corpsecret
        }
        # 发get请求
        r = requests.get(url=url, params=params)
        #获取token值
        self.token = r.json()['access_token']

    def test_create_department(self):
        """
        创建部门
        """
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
        #定义请求参数
        param = {
            "access_token": self.token
        }
        #定义请求体 data 是在Body里面的, param是放在url后面的
        data = {
                "name": "开发部门2",
                "name_en": "ABCDE",
                "parentid": 1,
                "order": 1,
                "id": 2
            }
        r = requests.post(url=url, json=data, params=param)
        # 打印响应数据
        print(r.json())
        #断言
        assert r.json()['errcode'] == 0 and r.json()['errmsg'] == "created"