import pytest
import requests


class TestToken():
    #前面定义的是参数的名称，后面定义的是参数值，以列表的形式 [(),()]
    @pytest.mark.parametrize(
        "corpid, corpsecret",
        [("wwa06955e5c907354a"),("_8yRExPVFzRiQhR7amDTLbBky58dBZqu2DuuDj019IU")],
        [(""),("_8yRExPVFzRiQhR7amDTLbBky58dBZqu2DuuDj019IU")],
        [("wwa06955e5c907354a"),("")],
    )
    def test_token(self,corpid, corpsecret):
        #正常操作
        # corpid = "wwa06955e5c907354a"
        # corpsecret = "_8yRExPVFzRiQhR7amDTLbBky58dBZqu2DuuDj019IU"
        # url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        # r = requests.get(url=url)
        # print(r.json())
        # assert r.json()['errcode'] == 0
        #缺必填项的操作 校验corpsecret 必填是否生效
        # corpid = "wwa06955e5c907354a"
        # corpsecret = "_8yRExPVFzRiQhR7amDTLbBky58dBZqu2DuuDj019IU"
        # url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}"
        # r = requests.get(url=url)
        # print(r.json())
        # assert r.json()['errcode'] == 41004
        #缺必填项的操作 校验corpid 必填是否生效
        # corpid = "wwa06955e5c907354a"
        # corpsecret = "_8yRExPVFzRiQhR7amDTLbBky58dBZqu2DuuDj019IU"
        # url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpsecret={corpsecret}"
        # r = requests.get(url=url)
        # print(r.json())
        # assert r.json()['errmsg'] == 'corpid missing'
        #一条条去试太麻烦，用参数化的办法
        t_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={self.corpid}&corpsecret={self.corpsecret}"
        r = requests.get(url=t_url)
        print(r.json())
        # assert r.json()['errcode'] == 0