
"""
编辑成员u你
"""
# from Python13_class.Page.member_invite_page import MemberInvitePage
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from Python13_class.Page.basepage import BasePage


class ContactEditPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver
    name_element = (MobileBy.XPATH, '//*[contains(@text,"姓名")]/../*[@text="必填"]')
    gender_element = (MobileBy.XPATH, '//*[@text="男"]')
    female_element = (MobileBy.XPATH, '//*[@text="女"]')
    male_element = (MobileBy.XPATH, '//*[@text="男"]')
    number_element = (MobileBy.XPATH,'//*[contains(@text,"手机") and @class="android.widget.TextView"]/..//*[@class="android.widget.EditText"]')
    save_element = (MobileBy.ID, 'com.tencent.wework:id/hvk')
    def edit_name(self,name):
        # self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"姓名")]/../*[@text="必填"]').send_keys(name)
        self.find_and_sendkeys(self.name_element,name)
        return self
    def edit_gender(self,gender):
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="男"]').click()
        self.find_and_click(self.gender_element)
        if gender == "女":
            # self.driver.find_element(MobileBy.XPATH, '//*[@text="女"]').click()
            self.find_and_click(self.female_element)
        else:
            # self.driver.find_element(MobileBy.XPATH, '//*[@text="男"]').click()
            # 加显式等待
            # element = WebDriverWait(self.driver, 5).until(lambda x: x.find_element(MobileBy.XPATH, '//*[@text="男"]'))
            # element = WebDriverWait(self.driver, 5).until(lambda x: x.self.find(self.male_element))
            # element.click()
            self.find_and_click(self.male_element)

        return self
    def edit_number(self,number):
        # self.driver.find_element(MobileBy.XPATH,'//*[contains(@text,"手机") and @class="android.widget.TextView"]/..//*[@class="android.widget.EditText"]').send_keys(
        #     number)
        self.find_and_sendkeys(self.number_element,number)
        return self

    def click_save(self):
        # self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/hvk').click()
        self.find_and_click(self.save_element)
        from Python13_class.Page.member_invite_page import MemberInvitePage
        return MemberInvitePage(self.driver)
