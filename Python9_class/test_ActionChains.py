import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep

from selenium.webdriver.common.keys import Keys


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        # self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()

    # 打开页面“http://sahitest.com/demo/clicks.htm”
    # 分别对 click me, dbl click me, right click me,执行点击双击右键操作
    @pytest.mark.skip
    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        # element_click = self.driver.find_element_by_xpath("/html/body/form/input[3]")
        element_click = self.driver.find_element_by_xpath("//input[@value='click me']")
        element_doubleclick = self.driver.find_element_by_xpath("//input[@value='dbl click me']")
        element_rightclick = self.driver.find_element_by_xpath("//input[@value='right click me']")
        action = ActionChains(self.driver)
        action.click(element_click)
        action.context_click(element_rightclick)
        action.double_click(element_doubleclick)
        sleep(3)
        action.perform()
        sleep(3)

    # 打开页面“http://www.baidu.com”
    # 把光标移动到 设置 位置
    @pytest.mark.skip
    def test_movetoelement(self):
        self.driver.get("http://www.baidu.com")
        sleep(3)
        ele = self.driver.find_element_by_id("s-usersetting-top")
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        sleep(3)
    # 打开页面“http://http://sahitest.com/demo/dragDropMooTools.htm”
    # 完成各种拖拽
    @pytest.mark.skip
    def test_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_element = self.driver.find_element_by_id("dragger")
        drop_element1 = self.driver.find_element_by_xpath("/html/body/div[2]")
        drop_element2 = self.driver.find_element_by_xpath("/html/body/div[3]")
        drop_element3 = self.driver.find_element_by_xpath("/html/body/div[4]")
        action = ActionChains(self.driver)
        #拖下来放第一个
        action.drag_and_drop(drag_element,drop_element1).perform()
        #拖下来放第二个
        action.click_and_hold(drag_element).release(drop_element2).perform()
        #拖下来放第3个
        action.click_and_hold(drag_element).move_to_element(drop_element3).release().perform()
        sleep(3)

    # 打开页面“http://sahitest.com/demo/label.htm”
    # 点击用户名的输入框，输入username， 空格，tom,删掉m
    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele = self.driver.find_element_by_xpath("/html/body/label[1]/input")
        ele.click()
        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).pause(1).perform()




    # if __name__ == "__main__":
    #     pytest.main(['-v','-s','test_ActionChains.py'])

