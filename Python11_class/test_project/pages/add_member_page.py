from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from Python11_class.test_project.pages.basepage import BasePage
from Python11_class.test_project.pages.contact_page import ContactPage


class AddMemberPage(BasePage):
    # _表示私有
    _username = (By.ID, "username")
    _calcel = (By.CSS_SELECTOR,"[node-type='cancel']")
    def add_member(self,name,acctid,phone):
        #  find_element(By.IF, "username")
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        # 用户名，账号，手机号 find 封装
        self.find(*self._username).send_keys(name)
        self.find(By.ID,"memberAdd_acctid").send_keys(acctid)
        self.find(By.ID,"memberAdd_phone").send_keys(phone)

        #用户名，账号，手机号 参数化
        # self.find_by_id(*self._username).send_keys(name)
        # self.find_by_id("memberAdd_acctid").send_keys(acctid)
        # self.find_by_id("memberAdd_phone").send_keys(phone)

        #用户名，账号，手机号 一个个输入
        # self.find_by_id("username").send_keys("哈利波特")
        # self.find_by_id("memberAdd_acctid").send_keys("excellent")
        # self.find_by_id("memberAdd_phone").send_keys("13333333333")

        #添加完之后还在当前页面，返回自己，方便调用
        #实现返回当前页面时依然可以实现链式调用
        #相当于别人调用是 add_member().save_member() =>self.save_member()
        return self

    def save_member(self):
        # self.find_by_css_selector('.js_btn_save').click()
        sleep(3)
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        # self.find_by_xpath('//*[@id="js_contacts358"]/div/div[2]/div/div[4]/div/form/div[1]/a[2]').click()
        sleep(3)
        return ContactPage(self.driver)

    def cancel_member(self):
        self.find(By.CSS_SELECTOR,'.js_btn_cancel').click()
        self.wait_for_clickable(self._calcel)
        self.find(*self._calcel).click()
        return ContactPage(self.driver)
