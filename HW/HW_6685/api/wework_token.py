import pytest

from HW.HW_6685.api.base_api import BaseApi

#企业微信独有的token需要放在url中进行传递,继承BaseApi,从而继承requests,jsonpath方法
class WeWork_token(BaseApi):
    def get_token(self,corpid,corpsecret):
        req = {
            "method":"get",
            "url":f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        }
        #用BaseApi的requests方法去获取token
        r = self.base_send_requests(req)
        self.token = r.json()["access_token"]
        #返回获取到的token
        return self.token