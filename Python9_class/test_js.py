import time

from Python9_class.base import Base
import pytest


class TestJS(Base):
    @pytest.mark.skip
    def test_js_scroll(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("selenium测试")
        # 用selenium driver定位
        # self.driver.find_element_by_id("su")
        # 在selenium里面执行js代码 去定位，记得加return 去返回值
        element = self.driver.execute_script('return document.getElementById("su")')
        time.sleep(3)
        element.click()
        # 在selenium里面执行js代码 去滑动到最底端
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        self.driver.find_element_by_xpath('//*[@id="page"]/div/a[10]').click()
        time.sleep(3)
        #for 循环去执行两个js命令,这样打印可以打印出所有 return的值
        for code in [
            "return document.title","return JSON.stringify(performance.timing)"
        ]:
            print(self.driver.execute_script(code))
        # 不用for循环，直接用分号隔开。这样打印只会打印第一个return的值
        # print(self.driver.execute_script("return document.title;return JSON.stringify(performance.timing)"))
    #利用selenium 来调用js  script 
    def test_datetime(self):
        self.driver.get("https://www.12306.cn/index/")
        self.driver.execute_script('a=document.getElementById("train_date");a.removeAttribute["readonly"]')
        self.driver.execute_script('document.getElementById("train_date").value="2020-11-10"')
        time.sleep(3)
        print(self.driver.execute_script('return document.getElementById("train_date").value'))
