
"""\
app.py 存放app一些特有的操作
比如：启动应用，重启应用，关闭应用，进入到首页
"""
from appium import webdriver

from Python13_class.Page.basepage import BasePage
from Python13_class.Page.main_page import MainPage


class App(BasePage):
    def start(self):
        """
        启动APP
        """
        if self.driver == None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "127.0.0.1:7555"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["noReset"] = "true"
            # 等待页面空闲的时间，动态页面默认等10s 太耗时了
            caps['settings[waitForIdleTimeout]'] = 1
            # 最重要！！户端代码与Appium Server建立连接,同时启动欢迎页
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(5)
        else:
            #用已有的driverlauch_app复用driver，并且不做任何初始化操作，不需要传入包名
            # self.driver.launch_app() 启动desirecap里面设置的appAcitivity
            # self.driver.start_activity(appPackage,appActivity),可以启动任何应用的页面
            self.driver.launch_app()
        return self
    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()
    def stop(self):
        self.driver.quit()
    def goto_main(self)->MainPage:
        """
        跳转到首页
        :return:
        """
        return MainPage(self.driver)