import pytest

from Python11_class.test_project.pages.main_page import MainPage
# 首先确定PO: Page Object 以及PO 之间关系
# 然后分别去每一个PO 定义方法
# 在test case 这一层就可以非常清楚地描述业务逻辑
#
class TestAddMember():
    def setup(self):
        self.main = MainPage()

    # @pytest.mark.parametrize(
    #     "name, acctid, phone", []
    # )
    def test_add_member(self):
        # 1. 从首页跳转到添加成员页面
        # 2. 添加成员，并且保存
        namelist = self.main.go_to_add_member().add_member("哈利波特","Excellent","13322228888").save_member().get_member_list()
        assert "哈利波特" in namelist
    def test_add_member_fail(self):

        # 1. 从首页跳转到添加成员页面
        # 2. 添加成员，并且保存
        namelist = self.main.go_to_add_member().add_member("哈利波特2","Excellent","13322228888").cancel_member().get_member_list()
        print(namelist)
        assert "哈利波特2" not in namelist



    def test_contact_member(self):
        self.main = MainPage()
        # 1. 从首页跳转到通讯录页面
        # 2. 跳转到添加成员页面
        # 3. 添加成员
        self.main.go_to_contact().go_to_add_member().add_member("哈利波特3","Excellent3","13322228788").save_member().get_member_list()

    def teardown(self):
        self.main.driver.quit()



    #
    # def setup(self):
    #     pass
    # def teardown(self):
    #     pass