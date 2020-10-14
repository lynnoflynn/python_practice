import time

from selenium.webdriver.common.by import By

from Python11_class.test_project.pages.basepage import BasePage


class ContactPage(BasePage):
    _add_member = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
    _calcel = (By.CSS_SELECTOR,"[node-type='cancel']")

    def go_to_add_member(self):
        #解决循环导入circular import，把导入放在方法里面
        from Python11_class.test_project.pages.add_member_page import AddMemberPage
        time.sleep(5)
        #确认添加成员按钮是可以点的
        self.find(*self._add_member).click()


        # self.wait_for_clickable(self._add_member)
        # #进入死循环
        #
        # while True:
        #     self.find(*self._add_member).click()
        #     #报错被捕获，执行except循环 点击找元素操作，直到找到为止
        #     try:
        #         #找到添加成员页面的某个元素
        #         res = self.find(*self._calcel)
        #         #如果存在的话久跳出循环，不存在就报错
        #         if res is not None:
        #             break
        #     except:
        #         print("暂时没找到")
        return AddMemberPage(self.driver)

        #因为check box一般是最慢的，所以先等checkbox加载，等加载完后其余的应该是可以点击的
        # self.wait_for_clickable((By.CSS_SELECTOR,".js_title .ww_checkbox "))
        return AddMemberPage(self.driver)

    def get_member_list(self):
        #返回一个列表
        ele = self.finds(By.CSS_SELECTOR,'.member_colRight_memberTable_td:nth-child(2)')
        return [name.text for name in ele]
        # list1=[]
        # for name in ele:
        #     list1.append(name.text)