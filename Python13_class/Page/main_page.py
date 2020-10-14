

"""
主页：暂时用到的有通讯录和工作台
"""
from appium.webdriver.common.mobileby import MobileBy

from Python13_class.Page.addresslist_page import AddressListPage
from Python13_class.Page.basepage import BasePage


class MainPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver
    addresslist_element = (MobileBy.XPATH, '//*[@text="通讯录"]')
    def goto_addresslist(self):
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        self.find_and_click(self.addresslist_element)
        return AddressListPage(self.driver)
    def goto_workbench(self):
        pass