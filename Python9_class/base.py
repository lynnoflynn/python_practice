from selenium import webdriver
import os

class Base():
    def setup(self):
        browser = os.getenv("browser")
        if browser == "firebox":
            self.driver = webdriver.Firefox()
            #若是没有配置环境变量，要单独指定driver 路径
            #self.driver = webdriver.Firefox(executable_path="C:\Software\Firefox_Driver\geckodriver-v0.27.0-win64")
        elif browser =="headless":
            self.driver = webdriver.PhantomJS()
        else:
            self.driver = webdriver.Chrome()
        #隐式等待是动态的等待，这里每0.5秒搜一下，搜到了就补等了，搜满5秒为止
        #最好是在实例化driver之后立刻设置
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()