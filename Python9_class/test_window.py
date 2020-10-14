from time import sleep

from selenium import webdriver

from Python9_class.base import Base

#学习窗口的切换
class TestWindow(Base):
    def test_window(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_xpath('//*[@id="u1"]/a').click()
        self.driver.find_element_by_xpath('//*[@id="passport-login-pop-dialog"]/div/div/div/div[3]/a').click()
        #这样会报错，因为跳转到了新的页面，而此时的driver代表的是当前的窗口
        #self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__userName"]').send_keys("username")
        windows = self.driver.window_handles
        #所以先进行窗口切换再去找输入框，-1是最后一个窗口
        self.driver.switch_to.window(windows[-1])
        #输入用户名和手机号
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__userName"]').send_keys("username")
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__phone"]').send_keys("13145678925")
        #切回来，0 是刚刚获取的第一个窗口
        sleep(2)
        self.driver.switch_to.window(windows[0])
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__footerULoginBtn"]').click()
        #点击登录之后 输入用户名和密码
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__userName"]').send_keys("login_username")
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__password"]').send_keys("login_password")
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__submit"]').click()
        sleep(3)