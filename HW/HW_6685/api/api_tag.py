from HW.HW_6685.api.wework_token import WeWork_token


#描述了创建标签，更新标签名字，删除标签 以及获取标签列表这些接口信息
#单纯针对每个接口的信息进行描述，与业务逻辑无关
# class Api_Tag继承class WeWork_token,从而获取token
# class WeWork_token继承了class BaseApi，可以获取requests,jsonpath方法
class Api_Tag(WeWork_token):
    #创建标签
    def create_tag(self,tag_name):
        #请求包体
        data = {
               "tagname": tag_name,
               "tagid": 12
            }
        #请求方式和地址
        req = {
                "method":"post",
                "url":f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token{self.token}",
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
    def get_tag_members(self):
        # 请求方式和地址
        req = {
                "method": "get",
                "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={self.token}"
            }
        # 用 class BaseApi 里面的方法
        r = self.base_send_requests(req)
        # 返回json()数据
        return r.json()