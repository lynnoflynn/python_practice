import requests
from requests.auth import HTTPBasicAuth

#认证体系
def test_auth():
    R = requests.get(url="http://httpbin.testing-studio.com/basic-auth/lynn/123456",
                 auth=HTTPBasicAuth("lynn","123456"))
    print(R.text)
