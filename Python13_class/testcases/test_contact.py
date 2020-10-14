from Python13_class.Page.app import App


class TestContact:

    def setup(self):
        """
        应用的启动
        :return:
        """
        self.app = App()
        self.main = self.app.start().goto_main()
    def teardown(self):
        """
        应用的关闭
        :return:
        """
        self.app.stop()
    def test_addcontact(self):
        name = "Ron9"
        gender = "男"
        number = "18201301261"
        #测试用例的编写只是关注流程
        #进入通讯录,添加成员，选择手动添加，编辑姓名性别电话，保存
        mypage = self.main.goto_addresslist().add_member().addcontact_manual()\
            .edit_name(name).edit_gender(gender).edit_number(number).click_save()
        mytoast = mypage.get_toast()
        assert "添加成功" == mytoast