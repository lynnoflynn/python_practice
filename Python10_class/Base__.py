from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Base():
    def setup_method(self,method):
        # 复用已有浏览器（节省时间，保留登录状态，操作记录。方便调试）
        # option = Options()
        # option.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=option)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        self.driver.quit()
