from time import sleep

from selenium.webdriver import ActionChains

from Python9_class.base import Base


class TestAlert(Base):
    def test_alert(self):
        #打开网页
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        #切换frame
        self.driver.switch_to_frame("iframeResult")
        #定位frame里面的元素
        ele1 = self.driver.find_element_by_id("draggable")
        ele2 = self.driver.find_element_by_id("droppable")
        #拖 ele1 到ele2
        action = ActionChains(self.driver)
        action.drag_and_drop(ele1,ele2).perform()
        #切换到alert 弹框并确认
        sleep(3)
        print("点击alert确认")
        self.driver.switch_to.alert.accept()
        #切换回来
        self.driver.switch_to_default_content()
        #再去点击 "点击运行"
        self.driver.find_element_by_xpath('//*[@id="submitBTN"]').click()
        sleep(3)

