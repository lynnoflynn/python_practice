from time import sleep

from Python9_class.base import Base
#多frame 的切换使用

class TestFrame(Base):
    def test_frame(self):
        #打开网页
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        #切换frame 方法1
        #self.driver.switch_to_frame("iframeResult")
        # 切换frame 方法2
        self.driver.switch_to.frame("iframeResult")
        print(self.driver.find_element_by_id("draggable").text)
        #切换回去父frame 方法一
        #self.driver.switch_to.parent_frame()
        # 切换回去默认的(父frame） 方法一
        self.driver.switch_to.default_content()
        print(self.driver.find_element_by_id("submitBTN").text)
        sleep(3)