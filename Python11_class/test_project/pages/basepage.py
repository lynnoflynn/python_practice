#重复的代码要被封装起来
#在这里可以完成初始化 跳过二维码，打开网页
#在这里可以定义一些公用的方法
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    _base_url=""
    def __init__(self,driver_base = None):
        #通过这个if语句 ，来阻止这个网页疯狂初始化
        # 避免driver的重复实例化
        # 一旦有了第一次的赋值，后面都不再去打开主页了
        if driver_base is None:
            option = Options()
            option.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=option)
        else:
            #这里这个WebDriver只是为了让IDE 能够帮忙提示
            self.driver: WebDriver = driver_base
        if self._base_url !="":
            self.driver.get(self._base_url)
        self.driver.implicitly_wait(5)

        #find element都被封装在这里了
    def find(self,by,value):
        return self.driver.find_element(by,value)

    def finds(self,by,value):
        return self.driver.find_elements(by,value)

    def wait_for_clickable(self,element):
        #显示等待元素可被点击
        return WebDriverWait(self.driver,10).until(ec.element_to_be_clickable(element))

    def wait(self,element):
        return WebDriverWait(self.driver,10).until(ec.presence_of_element_located(element))

