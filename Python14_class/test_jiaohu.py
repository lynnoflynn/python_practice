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
        desired_caps['deviceName'] = "A6"
        desired_caps['avd'] = "A6"

        desired_caps['appPackage'] = "com.xueqiu.android"
        desired_caps['appActivity'] = "com.xueqiu.android.main.view.MainActivity"
        desired_caps["noReset"] = "true"
        desired_caps['dontStopAppOnReset'] = 'true'
        # desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)
    def teardown(self):
        # self.driver.back()
        self.driver.quit()

    def test_mobile(self):
        # self.driver.make_gsm_call('13812341234',GsmCallActions.CALL)
        # self.driver.send_sms('13812341235','hello appium api')
        # self.driver.start_recording_screen()
        self.driver.set_network_connection(1)
        self.driver.get_screenshot_as_file('./photos/img.png')
        sleep(3)
        self.driver.set_network_connection(4)
        sleep(3)
        # self.driver.stop_recording_screen()
