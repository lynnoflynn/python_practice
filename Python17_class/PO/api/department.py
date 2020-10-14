import requests

from HW.HW_6685.api.wework_token import WeWork_token


class Department(WeWork_token):
    def create_department(self,department_id):
        # url_create = f'https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}'
        data = {
            "name": "Griffindor",
            "name_en": "ABCD",
            "parentid": 1,
            "order": 1,
            "id": department_id
        }
        req ={
            "method":"post",
            "url":f'https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}',
            "json": data
        }
        # r = requests.post(url=url_create, json=data)
        r = self.send_requests(req)
        #return他的返回体
        return r.json()
    def update_department(self,department_id):
        # url_update = f'https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}'
        data = {
            "id": department_id,
            "name": "lala",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1
        }
        req = {
            "method": "post",
            "url": f'https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}',
            "json": data
        }
        # r = requests.post(url=url_update, json=data)
        r = self.send_requests(req)
        return r.json()
    def delete_department(self,department_id):
        # url_delete = f'https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={department_id}'
        req = {
            "method": "get",
            "url": f'https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={department_id}'
        }

        # r = requests.get(url=url_delete)
        r = self.send_requests(req)
        return r.json()
    def get_department_list(self):
        # url_get_list = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        req = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        }
        r = self.send_requests(req)
        # r = requests.get(url=url_get_list)
        return r.json()

