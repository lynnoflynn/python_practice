# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

"""
改造1：使用pytest测试框架 
"""
class TestWebView:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "io.appium.android.apis"
        caps["appActivity"] = ".ApiDemos"
        caps["noReset"] = "true"
        #等待页面空闲的时间，动态页面默认等10s 太耗时了
        caps['settings[waitForIdleTimeout]'] = 1
        caps['chromedricerExecutable'] = 'C:/Software/Chromedriver2.24/chromedriver.exe'
        #最重要！！户端代码与Appium Server建立连接,同时启动欢迎页
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()


    def test_webview(self):
        self.driver.find_element_by_accessibility_id("Views").click()
        webview = "WebView"
        print(self.driver.contexts)
        #展示在页面上元素的才能被找到,滚动查找
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 f'.text("{webview}").instance(0));').click()
        # sleep(3)

        # self.driver.find_element(MobileBy.ID,'i_am_a_textbox').send_keys('this is a test string')
        # self.driver.find_element(MobileBy.ACCESSIBILITY_ID,'i am a link').click()
        # print(self.driver.page_source)
        print(self.driver.contexts)
        self.driver.switch_to.context(self.driver.contexts[-1])
        # self.driver.find_element(MobileBy.ID,'i_am_a_textbox').send_keys('this is a test string using chrome inspect')
        self.driver.find_element(MobileBy.ID,'i am a link').click()
        print(self.driver.page_source)
