from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from Python11_class.test_project.pages.add_member_page import AddMemberPage
from Python11_class.test_project.pages.basepage import BasePage
from Python11_class.test_project.pages.contact_page import ContactPage


class MainPage(BasePage):

    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    #元组
    _add_member = (By.CSS_SELECTOR, "[node-type='addmember']")
    _menu_contacts= (By.ID, "menu_contacts")
    def go_to_contact(self):
        self.find(*self._menu_contacts).click()
        #对ContactPage类进行实例化，表示业务逻辑的转换关系
        #类实例化以后，里面的方法都可以被调用
        return ContactPage(self.driver)

    def go_to_add_member(self):
        # *self.   解元组
        self.driver.find_element(*self._add_member).click()
        #对AddMemberPage类进行实例化，表示业务逻辑的转换关系
        return AddMemberPage(self.driver)