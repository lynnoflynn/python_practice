from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestTouchAction():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = "Android"
        desired_caps['platformVersion'] = 6.0
        desired_caps['deviceName'] = "127.0.0.1:7555"
        desired_caps['appPackage'] = "cn.kmob.screenfingermovelock"
        desired_caps['appActivity'] = "com.samsung.ui.MainActivity"
        desired_caps["noReset"] = "true"
        desired_caps['dontStopAppOnReset'] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()

    def test_touchaction_unlock(self):
        # self.driver.find_element_by_id()
        action = TouchAction(self.driver)
        action.press(x=118,y=183).wait(200).move_to(x=356,y=188).wait(200).move_to(x=598,y=173).wait(200).move_to(x=594,y=421).wait(200).move_to(x=598,y=669).wait(200).release().perform()
