import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver import TouchActions

class TestTouchAction():
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option("w3c",False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()

    def test_touchaction_scrollbottom(self):
        # 打开Chrome
        # 打开 URL: http://www.baidu.com
        # 向搜索框中输入"selenium测试"
        # 通过TouchAction 点击搜索栏
        # 滑动到底部，点击下一页
        # 关闭Chrome
        self.driver.get("http://www.baidu.com")
        ele_input = self.driver.find_element_by_id("kw")
        ele_search = self.driver.find_element_by_id("su")
        ele_input.send_keys("selenium测试")
        action = TouchActions(self.driver)
        action.tap(ele_search).perform()
        #滑动到底部 X 方向不需要滑动，Y 方向尽可能大
        action.scroll_from_element(ele_input,0,10000).perform()
        sleep(3)

