import requests

#自定义header
def test_demo():
    url="http://httpbin.testing-studio.com/cookies"
    #Cookie 不是Cookies，首字母一定要大写
    #header参数传递Cookie
    header={
        "Cookie":"hogwarts=school",
        'User-Agent': 'hogwarts'
            }

    r = requests.get(url=url,headers=header)
    print(r.request.headers)

#使用cookies参数进行传递
def test_demo():
    url="http://httpbin.testing-studio.com/cookies"
    #Cookie 不是Cookies，首字母一定要大写
    #header参数传递Cookie
    header={
        'User-Agent': 'hogwarts'
            }
    cookie_data = {
        "hogwarts":"school",
        "professor":"Snape"
    }
    r = requests.get(url=url,headers=header,cookies = cookie_data)
    print(r.request.headers)