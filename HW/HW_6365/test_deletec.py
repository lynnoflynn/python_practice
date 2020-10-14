from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestWeixin:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        #等待页面空闲的时间，动态页面默认等10s 太耗时了
        caps['settings[waitForIdleTimeout]'] = 1
        #最重要！！户端代码与Appium Server建立连接,同时启动欢迎页
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()

    def test_deletecontact(self):
        #联系人信息
        name = "Ron2"
        #找到通讯录并点击
        self.driver.find_element(MobileBy.XPATH,'//*[@text="通讯录"]').click()
        #找到搜索框并点击
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/hvn').click()
        #找到搜索框并输入 需要删除的联系人名字
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/gfs').send_keys(name)
        #在搜索结果里找到需要删除的人
        sleep(5)
        #千万记得s!!!! find element是对元素的操作，find elements是对列表的操作
        ele1 = self.driver.find_elements(MobileBy.XPATH, f'//*[@text="{name}"]')
        #先查找是否
        before = len(ele1)
        if before < 2:
            print("没有该联系人")
            return
        ele1[1].click()

        # self.driver.find_element(MobileBy.XPATH,f'//*[@text="{name}" and @class="android.widget.TextView"]').click()
        #点击右上角
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/hvd').click()
        # 点击编辑成员
        self.driver.find_element(MobileBy.XPATH, '//*[@text="编辑成员"]').click()
        #滚动查找删除成员并点击
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                  'new UiScrollable(new UiSelector()'
                                  '.scrollable(true).instance(0))'
                                  '.scrollIntoView(new UiSelector()'
                                  '.text("删除成员").instance(0));').click()
        # 点击确定
        self.driver.find_element(MobileBy.XPATH, '//*[@text="确定"]').click()
        # 在搜索结果里再次 搜索需要删除的人名
        sleep(5)
        ele2 = self.driver.find_elements(MobileBy.XPATH, f'//*[@text="{name}"]')
        after = len(ele2)

        assert before != after









        # self.driver.find_element(MobileBy.XPATH,'//*[@text="添加成员"]').click()
        #再多添加几个成员这个元素就找不到了，需要滚动查找
       #  self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
       #                           'new UiScrollable(new UiSelector()'
       #                           '.scrollable(true).instance(0))'
       #                           '.scrollIntoView(new UiSelector()'
       #                           '.text("添加成员").instance(0));').click()
       #  self.driver.find_element(MobileBy.XPATH,'//*[@text="手动输入添加"]').click()
       #  #“姓名”和“必填” 是同一个父节点
       #  self.driver.find_element(MobileBy.XPATH,'//*[contains(@text,"姓名")]/../*[@text="必填"]').send_keys(name)
       #  self.driver.find_element(MobileBy.XPATH,'//*[@text="男"]').click()
       #  if gender == "女":
       #      self.driver.find_element(MobileBy.XPATH, '//*[@text="女"]').click()
       #  else:
       #      # self.driver.find_element(MobileBy.XPATH, '//*[@text="男"]').click()
       #      # 加显式等待
       #      element = WebDriverWait(self.driver,5).until(lambda x:x.find_element(MobileBy.XPATH,'//*[@text="男"]'))
       #      element.click()
       # #分析“手机”和“手机号”关系，“手机”父节点/.. 的 孙子节点 //是”手机号“
       #  self.driver.find_element(MobileBy.XPATH,'//*[contains(@text,"手机") and @class="android.widget.TextView"]/..//*[@class="android.widget.EditText"]').send_keys(number)
       #  self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/hvk').click()
       #  # sleep(2)
       #  #打印页面布局看是否有toast
       #  # print(self.driver.page_source)
       #  my_toast = self.driver.find_element(MobileBy.XPATH,'//*[@class="android.widget.Toast"]').text
       #  assert "添加成功"== my_toast


