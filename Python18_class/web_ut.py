import configparser
import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class ISelenium(unittest.TestCase):
    def get_config(self):
        config = configparser.ConfigParser()
        config.read(os.path.join(os.environ['HOME'],'Iselenium.ini'))
        return config
    def teardown(self):
        self.driver.quit()
    def setup(self):
        config = self.get_config()
        try:
            using_headless = os.environ["using_headless"]
        except KeyError:
            using_headless = None
            print('没有配置环境变量 using_headless, 按照有界面方式运行自动化测试')
        chrome_options = Options()
        if using_headless is not None and using_headless.lower() == 'true':
            print('使用无界面方式运行')
            chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path=config.get('driver','chrome_driver'),options=chrome_options)
    def test_webui_1(self):
        self._test_baidu('今日头条','test_webui_1')
    def test_webui_2(self):
        self._test_baidu('王者荣耀','test_webui_2')
    def _test_baidu(self,search_keyword,testcase_name):
        self.driver.get("https://www.baidu.com")
        print("打开浏览器，访问百度")
        time.sleep(5)
        assert f'百度一下' in self.driver.title

        elem = self.driver.find_element_by_name("wd")
        elem.send_keys(f'{search_keyword}{Keys.RETURN}')
        print(f'搜索关键词~{search_keyword}')
        time.sleep(5)
        self.assertTrue(f'{search_keyword}' in self.driver.title, msg=f'{testcase_name}校验点pass')
