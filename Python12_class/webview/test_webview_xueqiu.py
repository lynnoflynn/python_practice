# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

"""
改造1：使用pytest测试框架 
"""
class TestWebView:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = "com.xueqiu.android.main.view.MainActivity"
        # caps["automationName"] = "appium"

        caps["noReset"] = "true"
        # caps["skipServerInstallation"] = "true"
        #等待页面空闲的时间，动态页面默认等10s 太耗时了
        caps['settings[waitForIdleTimeout]'] = 1
        caps['chromedriverExecutable'] = r'C:\Software\Chromedriver2.20\chromedriver.exe'
        #最重要！！户端代码与Appium Server建立连接,同时启动欢迎页
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()

    def test_webview(self):
        #点击交易
        self.driver.find_element(MobileBy.XPATH,'//*[@text="交易"]').click()
        # 点击‘A股开户’
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID,'A股开户').click()
        # a_locator = (MobileBy.XPATH,'//*[@id="Layout_app_3V4"]/div/div/ul/li[1]/div[2]/h1')
        print(self.driver.contexts)
        #切换上下文到webview界面
        self.driver.switch_to.context(self.driver.contexts[-1])
        # 有问题的一行：1：34：20
        # print(self.driver.window_handles)
        # WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(a_locator))
        # self.driver.find_element(*a_locator).click()
        print(self.driver.window_handles)
        #切换窗口
        # kaihu_window = self.driver.window_handles[-1]
        # self.driver.switch_to.window(kaihu_window)
        #显式等待
        phonenumber_locator = (MobileBy.ID,"phone-number")
        WebDriverWait(self.driver,60).until(expected_conditions.element_to_be_clickable(phonenumber_locator))
        #输入用户名和验证码，点击立即开户
        self.driver.find_element(*phonenumber_locator).send_keys("13312341234")
        self.driver.find_element(MobileBy.ID,"code").send_keys("1234")
        self.driver.find_element(MobileBy.CSS_SELECTOR,"body > div > div > div.form-wrap > div > div.btn-submit").click()
        # sleep(2)



