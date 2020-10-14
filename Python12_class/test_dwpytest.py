import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from hamcrest import *

class TestDW():

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

    def test_search(self):
        print("搜索测试用例")
        """
        1。 打开雪球app
        2。 点击搜索输入框
        3. 向搜索输输入框里面输入“阿里巴巴”
        4. 在搜索结果里面选择“阿里巴巴”，然后进行点击
        5.获取这只阿里巴巴的股价，并判断这只股价的价格>200
        """
        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        # 给一定的加载时间去找到那个元素
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        price = self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text
        price = float(price)
        assert price > 200

    def test_attr(self):
        """
            打开雪球应用
            定位首页搜索框
            判断搜索框是否可用，并看搜索框name属性值
            打印搜索框这个元素的左上角坐标和它的宽，高
            向搜索框输入alibaba
            判断【阿里巴巴】是否可见
            如果可见，打印【搜索成功】，若不可见，打印【搜索失败】
        """

        element = self.driver.find_element_by_id("com.xueqiu.android:id/home_search")
        self.driver.implicitly_wait(5)
        search_enabled = print(element.is_enabled())
        print(element.text)
        print(element.location)
        print(element.size)
        if search_enabled == True:
            element.click()
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
            alibaba_element = self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/name" and @text=”阿里巴巴“]')
            # alibaba_element.is_displayed()
            ele_display = alibaba_element.get_attribute("displayed")
            if ele_display == 'true':
                print("搜索成功")
            else:
                print("搜索失败")
    def test_touchaction(self):
        action = TouchAction(self.driver)
        #用当前屏幕的尺寸去定位，不需要根据设备的改变而改变
        window_rect = self.driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width/2)
        y1 = int(height*0.8)
        y2 = int(height*0.2)
        action.press(x=x1,y=y1).wait(200).move_to(x=x1,y=y2).release().perform()

    def test_get_current(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        # 给一定的加载时间去找到那个元素
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        current_price = self.driver.find_element_by_xpath('//*[@text=09988]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]').text
        current_price = float(current_price)
        expect_price = 200
        # assert current_price > 200
        assert_that(current_price,close_to(expect_price,expect_price*0.1))
    def test_myinfo(self):
        """
        1.点击我的，进入个人信息页面
        2.点击登录，进入登录页面
        3.入用户名和密码
        4.点击登录
        :return:
        """
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("账号密码登录")').click()

if __name__ == "__main__":
    pytest.main()