import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWD():

    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = "Android"
        desired_caps['platformVersion'] = 6.0
        desired_caps['deviceName'] = "127.0.0.1:7555"
        desired_caps['appPackage'] = "com.xueqiu.android"
        desired_caps['appActivity'] = "com.xueqiu.android.main.view.MainActivity"
        desired_caps["noReset"] = "true"
        desired_caps['dontStopAppOnReset'] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.back()
        self.driver.quit()

    def test_wait(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        # 给一定的加载时间去找到那个元素
        locator = (MobileBy.XPATH,'//*[@id="com.xueqiu.android:id/home_search"]')
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        current_price = self.driver.find_element_by_xpath(
            '//*[@text=09988]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]').text
        current_price = float(current_price)
        assert current_price > 200