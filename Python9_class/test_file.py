from Python9_class.base import Base
import pytest
from time import sleep

class TestFile(Base):
    #上传图片
    def test_file(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_xpath('//*[@id="sttb"]/img[1]').click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="stfile"]').send_keys("C:/Users/lynno/python_practice/Python9_class/ttt.PNG")
        sleep(2)
