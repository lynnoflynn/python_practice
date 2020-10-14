import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from hamcrest import *
from selenium.webdriver.common.by import By


class TestWebDriverWait():

    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = "Android"
        desired_caps['platformVersion'] = 6.0
        desired_caps['deviceName'] = "127.0.0.1:7555"
        desired_caps['appPackage'] = "com.xueqiu.android"
        desired_caps['appActivity'] = "com.xueqiu.android.main.view.MainActivity"
        desired_caps["noReset"] = True
        desired_caps['dontStopAppOnReset'] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)
    def teardown(self):
        # self.driver.back()
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/action_close").click()
        self.driver.quit()
    @pytest.mark.parametrize("searchkey,type,price",[
        ("alibaba","BABA", 270),
        ("xiaomi","01810", 23)
        ])
    def test_search(self,searchkey,type,price):
        """
        1.打开雪球
        2.店家搜索框
        3.输入搜索词‘alibaba’ 'xiaomi'
        4.点击第一个搜索结果
        5.判断股票价格
        :return:
        """
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/home_search").click()
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/search_input_text").send_keys(searchkey)
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/name").click()
        current_price = self.driver.find_element(MobileBy.XPATH,f"//*[@text='{type}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        current_price = float(current_price)
        print(f"当前价格{current_price}")
        assert_that(current_price,close_to(price,price*0.1))
