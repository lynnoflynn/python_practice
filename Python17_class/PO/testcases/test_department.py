import json

import yaml
# from jsonpath import jsonpath
# from jsonschema import validate

from Python17_class.PO.api.department import Department
# from Python17_class.PO.api.wework import WeWork


class TestDepartment():
    def setup_class(self):
        # wework = WeWork()
        self.department = Department()
        #通过传入不同的secret获取不同token权限，给不同的业务测试用例使用
        #当secret和业务紧密相关，应该抽离出来维护
        config_info = yaml.safe_load(open("config.yaml"))
        self.department.get_token(config_info["token"]["department_secret"])
        # self.token = wework.get_token()

    def test_create_department(self):
        self.department.create_department(3)
        list = self.department.get_department_list()
        print(list)
        # {'errcode': 0, 'errmsg': 'ok', 'department': [{'id': 1, 'name': 'Lynn--', 'parentid': 0, 'order': 100000000},
        #                                               {'id': 3, 'name': 'Griffindor', 'parentid': 1, 'order': 1,
        #                                                'name_en': 'ABCD'}]}
        name = self.department.base_jsonpath(list,"$..name")
        # name = jsonpath(list,"$..name")
        assert "Griffindor" in name
        # assert list["department"][1]["name"] == "Griffindor"

    def test_update_department(self):
        self.department.update_department(3)
        list = self.department.get_department_list()
        print(list)
        name = self.department.base_jsonpath(list, "$..name")
        # name = jsonpath(list, "$..name")
        assert "lala" in name
        # assert list["department"][1]["name"] == "lala"

    def test_delete_department(self):
        #删除id 为3的部门
        self.department.delete_department(3)
        #获取部门所有信息
        list = self.department.get_department_list()
        # print(list)
        #使用jsonpath提取出所有的部门id
        department_id = self.department.base_jsonpath(list,"$..id")
        # department_id = jsonpath(list,"$..id")
        assert 3 not in department_id
        # assert len(list["department"])== 1

    def test_get_department(self):
        r = self.department.get_department_list()
        get_list_schema = json.load(open("./json_schema/get_list_schema.json"))
        self.department.base_jsonschema(r,get_list_schema)
        # validate(r,get_list_schema)




