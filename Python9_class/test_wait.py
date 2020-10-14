from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")

    def test_wait(self):
        # self.driver.find_element(By.XPATH, "//*[@id='kw']").send_keys("霍格沃兹测试学院")
        # self.driver.find_element(By.ID, "kw").send_keys("霍格沃兹测试学院")
        # self.driver.find_element(By.CSS_SELECTOR, "#kw").send_keys("霍格沃兹测试学院")
        self.driver.find_element(By.CSS_SELECTOR, "[id=kw]").send_keys("霍格沃兹测试学院")
        self.driver.find_element(By.ID, "su").click()