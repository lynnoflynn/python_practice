from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestGetAttr():
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
        # self.driver.quit()
        pass

    def test_get_attr(self):
        search_ele = self.driver.find_element_by_id("com.xueqiu.android:id/home_search")
        print(search_ele.get_attribute("content-desc"))
        print(search_ele.get_attribute("resource-id"))
        print(search_ele.get_attribute("enabled"))
        print(search_ele.get_attribute("clickable"))
        print(search_ele.get_attribute("bounds"))
