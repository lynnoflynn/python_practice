import requests

from Python17_class.PO.api.base_api import BaseApi


class WeWork(BaseApi):
    def get_token(self,corp_secret):
        #token的定义
        corpid = "wwa06955e5c907354a"
        # corpsecret = "_8yRExPVFzRiQhR7amDTLbBky58dBZqu2DuuDj019IU"
        #get_token的请求信息
        req = {
            "method" : "get",
            "url" : f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corp_secret}"
            }
        # url_token = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        # r = requests.get(url=url_token)
        r = self.send_requests(req)
        self.token = r.json()["access_token"]
        return self.token
