import pytest
import requests


class TestToken():
    #前面定义的是参数的名称，后面定义的是参数值，以列表的形式，列表嵌套元组 [("",""),("","")]
    @pytest.mark.parametrize(
        "corpid, corpsecret,errmsg",
        [("wwa06955e5c907354a","_8yRExPVFzRiQhR7amDTLbBky58dBZqu2DuuDj019IU","ok"),
        ("","_8yRExPVFzRiQhR7amDTLbBky58dBZqu2DuuDj019IU","corpid missing"),
        ("wwa06955e5c907354a","","corpsecret missing")],
    )
    #在定义方但时，需要定义出来pytest装饰器中定义的形参
    def test_token(self,corpid, corpsecret,errmsg):
        #一条条去试太麻烦，用参数化的办法
        t_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        r = requests.get(url=t_url)
        print(r.json())
        assert r.json()['errmsg'] == errmsg