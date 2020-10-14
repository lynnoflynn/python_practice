#模块级别setup
def setup_module():
    print("模块级别setup")
def teardown_module():
    print("模块级别teardown")


# 函数级别setup
def setup_function():
    print("函数级别的setup")
def test_func1():
    print("测试 func1")
def teardown_function(self):
    print("函数级别的teardown")
#不同的类有相同的方法是可以允许的
class TestDemo1:
    def setup_class(self):
        print("类级别的setup")
    def teardown_class(self):
        print("类级别的teardown")
    def setup(self):
        print("方法级别的setup")
    def teardown(self):
        print("方法级别的teardown")

    def test_demo1(self):
        print("testdemo1")
    def test_demo2(self):
        print("testdemo2")
    def test_demo3(self):
        print("testdemo3")
class TestDemo2:
    def setup_class(self):
        print("类级别的setup")
    def teardown_class(self):
        print("类级别的teardown")
    def setup(self):
        print("方法级别的setup")
    def teardown(self):
        print("方法级别的teardown")

    def test_demo1(self):
        print("testdemo1")
    def test_demo2(self):
        print("testdemo2")
    def test_demo3(self):
        print("testdemo3")
# 类级别的setup teardown直在最前最后，方法级别在每个方法前后都setup teardown

# test_setup.py::test_func1 模块级别setup
# 函数级别的setup
# PASSED                                         [ 14%]测试 func1
# 函数级别的teardown
#
# test_setup.py::TestDemo1::test_demo1 类级别的setup
# 方法级别的setup
# PASSED                              [ 28%]testdemo1
# 方法级别的teardown
#
# test_setup.py::TestDemo1::test_demo2 方法级别的setup
# PASSED                              [ 42%]testdemo2
# 方法级别的teardown
#
# test_setup.py::TestDemo1::test_demo3 方法级别的setup
# PASSED                              [ 57%]testdemo3
# 方法级别的teardown
# 类级别的teardown
#
# test_setup.py::TestDemo2::test_demo1 类级别的setup
# 方法级别的setup
# PASSED                              [ 71%]testdemo1
# 方法级别的teardown
#
# test_setup.py::TestDemo2::test_demo2 方法级别的setup
# PASSED                              [ 85%]testdemo2
# 方法级别的teardown
#
# test_setup.py::TestDemo2::test_demo3 方法级别的setup
# PASSED                              [100%]testdemo3
# 方法级别的teardown
# 类级别的teardown
# 模块级别teardown