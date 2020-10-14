import requests
import pytest
#创建部门->更新部门->删除部门

class TestDepartment():
    def setup_class(self):
        corpid = "wwa06955e5c907354a"
        corpsecret = "_8yRExPVFzRiQhR7amDTLbBky58dBZqu2DuuDj019IU"
        url_t = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        r = requests.get(url=url_t)
        self.token = r.json()["access_token"]
        self.id = 2
    def test_create_department(self):
        url_create = f'https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}'
        data = {
                "name": "Griffindor",
                "name_en": "ABCD",
                "parentid": 1,
                "order": 1,
                "id": self.id
        }
        #因为所有的接口需使用HTTPS协议、JSON数据格式、UTF8编码。接口说明格式如下：
        #所以在传请求体的时候，用JSON参数
        r1 = requests.post(url=url_create,json=data)
        print(r1.json())

        #下面这个断言不靠谱，可能提示成功，但是实际上并没有成功
        assert r1.json()["errmsg"] == "created"
        #可以用获取部门列表去确认是否创建成功.只有创建成功了，获取才能成功
        url_get_list = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        r2 = requests.get(url=url_get_list)
        print(r2.json())
        #通过查询部门列表接口的返回值，实现查看部门是否新建成功
        assert r2.json()["department"][1]["name"] =="Griffindor"
    def test_update_department(self):
        url_update = f'https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}'
        data = {
               "id": self.id,
               "name": "lala",
               "name_en": "RDGZ",
               "parentid": 1,
               "order": 1
            }
        requests.post(url=url_update,json=data)

        # 可以用获取部门列表去确认是否创建成功.只有创建成功了，获取才能成功
        url_get_list = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        r2 = requests.get(url=url_get_list)
        print(r2.json())
        assert r2.json()["department"][1]["name"] == "lala"

    def test_delete_department(self):
        url_delete = f'https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={self.id}'
        requests.get(url=url_delete)
        url_get_list = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        r2 = requests.get(url=url_get_list)
        print(r2.json())
        assert len(r2.json()["department"])== 1


