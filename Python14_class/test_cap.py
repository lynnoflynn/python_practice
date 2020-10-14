from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.extensions.android.gsm import GsmCallActions
from hamcrest import *

class TestDW():

    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = "Android"
        desired_caps['platformVersion'] = 6.0
        desired_caps['deviceName'] = "emulator-5554"
        #指定想要的设备，让appium进行读取
        desired_caps['udid'] = "emulator-5554"
        #自动点掉一些弹框
        desired_caps['autoGrantPermissions'] = True
        #保留登录缓存等信息
        desired_caps["noReset"] = "true"
        #不要关闭APP再启动,提升速度
        desired_caps['dontStopAppOnReset'] = True

        desired_caps['avd'] = "A6"
        desired_caps['appPackage'] = "com.xueqiu.android"
        desired_caps['appActivity'] = "com.xueqiu.android.main.view.MainActivity"
        #5 分钟之内都不会报超时异常
        desired_caps['newCommandTimeout'] = 300


        # desired_caps['skipDeviceInitialization'] = 'true'
        # desired_caps['unicodeKeyBoard'] = 'true'
        # desired_caps['resetKeyBoard'] = 'true'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)
    def teardown(self):
        # self.driver.back()
        self.driver.quit()

    def test_mobile(self):

