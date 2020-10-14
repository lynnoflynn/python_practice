"""
基类：用来封装最基本的方法
初始化driver，find，显式等待。。
"""
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver:WebDriver=None):
        self.driver = driver
    def find(self,locator):
        #默认在传过来的是元组类型,调用的时候进行解包处理
        return self.driver.find_element(*locator)

    def find_and_click(self,locator):
        self.find(locator).click()

    def find_and_sendkeys(self,locator,value):
        self.find(locator).send_keys(value)

    def find_and_get_text(self,locator):
        return self.find(locator).text

    def find_by_scroll_and_click(self,text):
        ele = (MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 f'.text("{text}").instance(0));')
        self.find_and_click(ele)

    def gettoast_text(self):
        ele1 = (MobileBy.XPATH, '//*[@class="android.widget.Toast"]')
        return self.find_and_get_text(ele1)
        # mytoast = self.find(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text




