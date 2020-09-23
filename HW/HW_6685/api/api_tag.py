

#描述了创建标签，更新标签名字，删除标签 以及获取标签列表这些接口信息
#单纯针对每个接口的信息进行描述，与业务逻辑无关
# class Api_Tag继承class WeWork_token,从而获取token
# class WeWork_token继承了class BaseApi，可以获取requests,jsonpath方法
from HW.HW_6685.api.wework_token import WeWorkToken


class Api_Tag(WeWorkToken):
    #创建标签
    def create_tag(self,tag_name,tag_id):
        #请求包体
        data = {
               "tagname": tag_name,
               "tagid": tag_id
            }
        #请求方式和地址
        req = {
                "method":"post",
                "url":f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={self.token}",
                "json": data
            }
        #用 class BaseApi 里面的方法
        r = self.base_send_requests(req)
        # 返回json()数据
        return r.json()
    #更新标签名字
    def update_tag(self,tag_id,tag_name):
        # 请求包体
        data = {
                "tagid": tag_id,
                "tagname": tag_name
             }
        # 请求方式和地址
        req = {
                "method": "post",
                "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={self.token}",
                "json": data
            }
        # 用 class BaseApi 里面的方法
        r = self.base_send_requests(req)
        # 返回json()数据
        return r.json()

    #删除标签
    def delete_tag(self,tag_id):
        # 请求方式和地址
        req = {
                "method": "get",
                "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={self.token}&tagid={tag_id}"
            }
        # 用 class BaseApi 里面的方法
        r = self.base_send_requests(req)
        # 返回json()数据
        return r.json()

    #获取标签列表
    def get_tag_member_list(self):
        # 请求方式和地址
        req = {
                "method": "get",
                "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={self.token}"
            }
        # 用 class BaseApi 里面的方法
        r = self.base_send_requests(req)
        # 返回json()数据
        return r.json()

    #增加标签成员
    def add_tag_member(self,tag_id):
        # 请求包体
        data = {
                "tagid": tag_id,
                "userlist":[ "Harry","Ron"],
                "partylist": [4]
                 }
        # 请求方式和地址
        req = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers?access_token={self.token}",
            "json": data
        }
        # 用 class BaseApi 里面的方法
        r = self.base_send_requests(req)
        # 返回json()数据
        return r.json()

    # 获取标签成员
    def get_tag_member(self,tag_id):
        # 请求方式和地址
        req = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token={self.token}&tagid={tag_id}",
        }
        # 用 class BaseApi 里面的方法
        r = self.base_send_requests(req)
        # 返回json()数据
        return r.json()