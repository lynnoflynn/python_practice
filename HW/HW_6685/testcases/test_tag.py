import pytest

from HW.HW_6685.api.api_tag import Api_Tag
#test cases: 1.业务接口逻辑拼接；2，单接口字段校验；3，断言
# 参数化,业务逻辑的部分属于case层级,不能放在接口里面

class TestTag():
    #需要初始化的操作定义在setup方法里
    # 参数化:前面定义的是参数的名称，后面定义的是参数值，以列表的形式，列表嵌套元组 [("",""),("","")]
    def setup_class(self):
        self.tag = Api_Tag()
        corpid = "wwa06955e5c907354a"
        corpsecret = "_8yRExPVFzRiQhR7amDTLURDjo1JNSjYLg3cWD2VJoI"
        self.tag.get_token(corpid,corpsecret)

    # 参数化
    @pytest.mark.parametrize("tagname, tagid",
                           [("olg_tag1", "12"),
                            ("olg_tag2","13"),
                            ("olg_tag3","14")])
    # 增加标签
    def test_create_tag(self,tagname,tagid):
        #新建标签
        self.tag.create_tag(tagname,tagid)
        #获取标签列表
        list = self.tag.get_tag_member_list()
        print(list)
        tagname = self.tag.base_json_path(list,"$..tagname")
        #断言：新增的标签是否在标签列表里
        assert 'olg_tag1' in tagname

    # 增加标签成员
    def test_get_tag_list(self):
        # 新建标签成员
        self.tag.add_tag_member(12)
        # 获取标签列表
        list = self.tag.get_tag_member(12)
        print(list)
        name = self.tag.base_json_path(list, "$..name")
        # 断言：新增的标签是否在标签列表里
        assert 'Harry' in name

    #修改标签
    def test_update_tag(self):
        # 更新标签
        self.tag.update_tag(12,'I_am_a_new_tag')
        # 获取标签列表
        list = self.tag.get_tag_member_list()
        print(list)
        tagname = self.tag.base_json_path(list,"$..tagname")
        # 断言：新增的标签是否在标签列表里
        assert 'I_am_a_new_tag' in tagname

    #删除标签
    def test_delete_tag(self):
        # 更新标签
        self.tag.delete_tag(12)
        # 获取标签列表
        list = self.tag.get_tag_member_list()
        print(list)
        taglist = self.tag.base_json_path(list,"$..taglist")
        # 断言：新增的标签是否在标签列表里
        assert 12 not in taglist

