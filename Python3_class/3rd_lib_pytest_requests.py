import requests
#r=requests.get("http://baidu.com")
r=requests.post('http://httpbin.org/post',data={'key':'value'})
print(r.text)