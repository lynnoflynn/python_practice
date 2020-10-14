# 企业ID： wwa06955e5c907354a
# secret: _8yRExPVFzRiQhR7amDTLfNxuqsQYDdqIqmmEqRn14o
import requests

class TestToken():

    def test_get_token(self):
        """
        获取 access_token
        """
        #定义凭证
        corpid = "wwa06955e5c907354a"
        corpsecret = "_8yRExPVFzRiQhR7amDTLfNxuqsQYDdqIqmmEqRn14o"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        #发get请求
        r = requests.get(url=url)
        #打印响应数据
        print(r.json())

    def test_token_param(self):
        """
        获取 token的第二章形式
        """
        # 定义凭证
        corpid = "wwa06955e5c907354a"
        corpsecret = "_8yRExPVFzRiQhR7amDTLfNxuqsQYDdqIqmmEqRn14o"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        #定义请求参数
        params = {
            "corpid": corpid,
            "corpsecret": corpsecret
        }
        #发get请求
        r = requests.get(url=url,params=params)
        print(r.json())