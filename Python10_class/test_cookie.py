import shelve
from time import sleep

import pytest

from Python10_class.Base__ import Base


class TestCookie(Base):
    @pytest.mark.skip
    #理解cookie
    def test_cookie(self):
        # cookies = self.driver.get_cookies()
        # print (cookies)
        #带有登录信息的cookie
        cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
          'value': '1688853995496277'},
         {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
          'value': '1688853995496277'},
         {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
          'value': '15157395163103104'},
         {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
          'value': 'DoaiSt1xB_tLwOlTdAZu3NxJfAYYU8NEH4XN-hCLMykFrD8tcv1cs2A5DFG78E8gNz6GuB9arUXlTECzAzJXYT4woPGy0KhzdS-Firlv24gP-vSF3q6YlohGMVQxXQoiW3vi6nyzLFwLXEnU7sUbgA2wz3Ml9VQw4NMDUNrReoLr3BRQ-HB2vZvYKrT6hkt5aerA1mMwtzJmURl0QCant681xK0VccZkcjqexpQKEP9sl8iCGn1xEIad5YviLcnDYQ8jdw2fA97oOwqCE2jcsA'},
         {'domain': '.qq.com', 'httpOnly': False, 'name': '_qpsvr_localtk', 'path': '/', 'secure': False,
          'value': '0.5703872673364825'},
         {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
          'value': 'r3YSNSY1CLSX2MNDPlkf3nHanqwXGq_ccYzTftb1uZgMbVZ5IjHGZJactfJs-FPp'},
         {'domain': '.qq.com', 'httpOnly': False, 'name': 'pgv_info', 'path': '/', 'secure': False,
          'value': 'ssid=s6662131712'},
         {'domain': '.qq.com', 'expiry': 1914235914, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/',
          'secure': False, 'value': '9fa084b2dc101a1b'},
         {'domain': '.work.weixin.qq.com', 'expiry': 1630881869, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/',
          'secure': False, 'value': '0'},
         {'domain': '.work.weixin.qq.com', 'expiry': 1602107515, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
          'path': '/', 'secure': False, 'value': 'zh-cn'},
         {'domain': '.qq.com', 'expiry': 1606729226, 'httpOnly': False, 'name': 'psrf_qqaccess_token', 'path': '/',
          'secure': False, 'value': '22609EBD5C1776465D1001FFE810033B'},
         {'domain': 'work.weixin.qq.com', 'expiry': 1599547027, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
          'secure': False, 'value': '6tedge9'},
         {'domain': '.qq.com', 'expiry': 1606729226, 'httpOnly': False, 'name': 'psrf_qqopenid', 'path': '/',
          'secure': False, 'value': '482FD162750409476CDB9C26B59787C7'},
         {'domain': '.qq.com', 'expiry': 1606729226, 'httpOnly': False, 'name': 'tmeLoginType', 'path': '/',
          'secure': False, 'value': '2'},
         {'domain': '.qq.com', 'expiry': 1606729226, 'httpOnly': False, 'name': 'euin', 'path': '/', 'secure': False,
          'value': 'oiSF7iSPoKCP'},
         {'domain': '.qq.com', 'expiry': 1606729226, 'httpOnly': False, 'name': 'psrf_qqunionid', 'path': '/',
          'secure': False, 'value': ''},
         {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
          'value': 'a4975804'},
         {'domain': '.qq.com', 'expiry': 1606729226, 'httpOnly': False, 'name': 'psrf_access_token_expiresAt',
          'path': '/', 'secure': False, 'value': '1606729230'},
         {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
          'value': 'DYLxiMznQq'},
         {'domain': '.qq.com', 'expiry': 1606729226, 'httpOnly': False, 'name': 'psrf_qqrefresh_token', 'path': '/',
          'secure': False, 'value': 'C6E78B5E3CB1CA37416C8EAF024D5F4C'},
         {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
          'value': '1970324949161122'},
         {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
          'secure': False, 'value': '3266583356'},
         {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False,
          'value': '8911074304'},
         {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/',
          'secure': False, 'value': '378774164'},
         {'domain': '.qq.com', 'expiry': 2147483637, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
          'value': 'b273b620a41fa39854f725db88c344498f6c23af901fb771d3c985854ff671ab'},
         {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
          'value': '1'},
         {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
          'value': 'direct'}]
        #打开页面，需要登录
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        #给页面带有登录信息的cookie
        #cookies是一个列表，里面有多个字典。add_cookie只支持字典 不支持列表 所以用for循环

        for cookie in cookies:
            # cookie不支持浮点数，expiry可能会是float，它又不重要，为防报错，可以提前删
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        #现在再去那个页面，就已经登录了
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(3)
    # 在cookie基础上 加上点击添加联系人 然后上传文件，然后确认上传的文件是否正确
    @pytest.mark.skip
    def test_importcontact(self):
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688853995496277'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688853995496277'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '15157395163103104'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'DoaiSt1xB_tLwOlTdAZu3NxJfAYYU8NEH4XN-hCLMykFrD8tcv1cs2A5DFG78E8gNz6GuB9arUXlTECzAzJXYT4woPGy0KhzdS-Firlv24gP-vSF3q6YlohGMVQxXQoiW3vi6nyzLFwLXEnU7sUbgA2wz3Ml9VQw4NMDUNrReoLr3BRQ-HB2vZvYKrT6hkt5aerA1mMwtzJmURl0QCant681xK0VccZkcjqexpQKEP9sl8iCGn1xEIad5YviLcnDYQ8jdw2fA97oOwqCE2jcsA'},
            {'domain': '.qq.com', 'httpOnly': False, 'name': '_qpsvr_localtk', 'path': '/', 'secure': False,
             'value': '0.5703872673364825'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'r3YSNSY1CLSX2MNDPlkf3nHanqwXGq_ccYzTftb1uZgMbVZ5IjHGZJactfJs-FPp'},
            {'domain': '.qq.com', 'httpOnly': False, 'name': 'pgv_info', 'path': '/', 'secure': False,
             'value': 'ssid=s6662131712'},
            {'domain': '.qq.com', 'expiry': 1914235914, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/',
             'secure': False, 'value': '9fa084b2dc101a1b'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1630881869, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/',
             'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1602107515, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh-cn'},
            {'domain': '.qq.com', 'expiry': 1606729226, 'httpOnly': False, 'name': 'psrf_qqaccess_token', 'path': '/',
             'secure': False, 'value': '22609EBD5C1776465D1001FFE810033B'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1599547027, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '6tedge9'},
            {'domain': '.qq.com', 'expiry': 1606729226, 'httpOnly': False, 'name': 'psrf_qqopenid', 'path': '/',
             'secure': False, 'value': '482FD162750409476CDB9C26B59787C7'},
            {'domain': '.qq.com', 'expiry': 1606729226, 'httpOnly': False, 'name': 'tmeLoginType', 'path': '/',
             'secure': False, 'value': '2'},
            {'domain': '.qq.com', 'expiry': 1606729226, 'httpOnly': False, 'name': 'euin', 'path': '/', 'secure': False,
             'value': 'oiSF7iSPoKCP'},
            {'domain': '.qq.com', 'expiry': 1606729226, 'httpOnly': False, 'name': 'psrf_qqunionid', 'path': '/',
             'secure': False, 'value': ''},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a4975804'},
            {'domain': '.qq.com', 'expiry': 1606729226, 'httpOnly': False, 'name': 'psrf_access_token_expiresAt',
             'path': '/', 'secure': False, 'value': '1606729230'},
            {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
             'value': 'DYLxiMznQq'},
            {'domain': '.qq.com', 'expiry': 1606729226, 'httpOnly': False, 'name': 'psrf_qqrefresh_token', 'path': '/',
             'secure': False, 'value': 'C6E78B5E3CB1CA37416C8EAF024D5F4C'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970324949161122'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '3266583356'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': False,
             'value': '8911074304'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/',
             'secure': False, 'value': '378774164'},
            {'domain': '.qq.com', 'expiry': 2147483637, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': 'b273b620a41fa39854f725db88c344498f6c23af901fb771d3c985854ff671ab'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'}]
        # 打开页面，需要登录
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 给页面带有登录信息的cookie
        # cookies是一个列表，里面有多个字典。add_cookie只支持字典 不支持列表 所以用for循环

        for cookie in cookies:
            # cookie不支持浮点数，expiry可能会是float，它又不重要，为防报错，可以提前删
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        # 现在再去那个页面，就能登录了 因为cookie信息在里面了
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element_by_css_selector(".index_service_cnt_itemWrap:nth-child(2)").click()

        self.driver.find_element_by_id("js_upload_file_input").send_keys("C:/Users/lynno/OneDrive/Desktop/霍格沃茨笔记.xlsx")
        #拿到文本属性，然后进行断言，判断上传的文档是不是 “霍格沃茨笔记.xlsx”
        assert "霍格沃茨笔记.xlsx" == self.driver.find_element_by_id("upload_file_name").text
        sleep(3)
    #shelve 是python提供的内置模块，相当于小型的数据库
    #实现cookie数据的持久化储存
    def test_shelve(self):
        # cookies = [
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
        #      'value': '1688853995496277'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
        #      'value': '1688853995496277'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
        #      'value': '15157395163103104'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
        #      'value': 'DoaiSt1xB_tLwOlTdAZu3NxJfAYYU8NEH4XN-hCLMykFrD8tcv1cs2A5DFG78E8gNz6GuB9arUXlTECzAzJXYT4woPGy0KhzdS-Firlv24gP-vSF3q6YlohGMVQxXQoiW3vi6nyzLFwLXEnU7sUbgA2wz3Ml9VQw4NMDUNrReoLr3BRQ-HB2vZvYKrT6hkt5aerA1mMwtzJmURl0QCant681xK0VccZkcjqexpQKEP9sl8iCGn1xEIad5YviLcnDYQ8jdw2fA97oOwqCE2jcsA'},
        #     {'domain': '.qq.com', 'httpOnly': False, 'name': '_qpsvr_localtk', 'path': '/', 'secure': False,
        #      'value': '0.5703872673364825'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
        #      'value': 'r3YSNSY1CLSX2MNDPlkf3nHanqwXGq_ccYzTftb1uZgMbVZ5IjHGZJactfJs-FPp'},
        #     {'domain': '.qq.com', 'httpOnly': False, 'name': 'pgv_info', 'path': '/', 'secure': False,
        #      'value': 'ssid=s6662131712'},
        #     {'domain': '.qq.com', 'expiry': 1914235914, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/',
        #      'secure': False, 'value': '9fa084b2dc101a1b'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1630881869, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
        #      'path': '/',
        #      'secure': False, 'value': '0'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1602107515, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
        #      'path': '/', 'secure': False, 'value': 'zh-cn'},
        #     {'domain': '.qq.com', 'expiry': 1606729226, 'httpOnly': False, 'name': 'psrf_qqaccess_token', 'path': '/',
        #      'secure': False, 'value': '22609EBD5C1776465D1001FFE810033B'},
        #     {'domain': 'work.weixin.qq.com', 'expiry': 1599547027, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
        #      'secure': False, 'value': '6tedge9'},
        #     {'domain': '.qq.com', 'expiry': 1606729226, 'httpOnly': False, 'name': 'psrf_qqopenid', 'path': '/',
        #      'secure': False, 'value': '482FD162750409476CDB9C26B59787C7'},
        #     {'domain': '.qq.com', 'expiry': 1606729226, 'httpOnly': False, 'name': 'tmeLoginType', 'path': '/',
        #      'secure': False, 'value': '2'},
        #     {'domain': '.qq.com', 'expiry': 1606729226, 'httpOnly': False, 'name': 'euin', 'path': '/', 'secure': False,
        #      'value': 'oiSF7iSPoKCP'},
        #     {'domain': '.qq.com', 'expiry': 1606729226, 'httpOnly': False, 'name': 'psrf_qqunionid', 'path': '/',
        #      'secure': False, 'value': ''},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
        #      'value': 'a4975804'},
        #     {'domain': '.qq.com', 'expiry': 1606729226, 'httpOnly': False, 'name': 'psrf_access_token_expiresAt',
        #      'path': '/', 'secure': False, 'value': '1606729230'},
        #     {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
        #      'value': 'DYLxiMznQq'},
        #     {'domain': '.qq.com', 'expiry': 1606729226, 'httpOnly': False, 'name': 'psrf_qqrefresh_token', 'path': '/',
        #      'secure': False, 'value': 'C6E78B5E3CB1CA37416C8EAF024D5F4C'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
        #      'value': '1970324949161122'},
        #     {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
        #      'secure': False, 'value': '3266583356'},
        #     {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
        #      'secure': False,
        #      'value': '8911074304'},
        #     {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/',
        #      'secure': False, 'value': '378774164'},
        #     {'domain': '.qq.com', 'expiry': 2147483637, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
        #      'value': 'b273b620a41fa39854f725db88c344498f6c23af901fb771d3c985854ff671ab'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
        #      'value': '1'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
        #      'value': 'direct'}]
        # #把数据存在小型数据库里
        # db = shelve.open("./My_DBs/cookies")
        # #刚才的一长串列表 放在db 里
        # db["cookie"] = cookies
        # db.close()
        # 打开数据库
        db = shelve.open("./My_DBs/cookies")
        #拿数据 并把数据存在cookies里面
        cookies = db["cookie"]
        #要先打开对应域名的网页，才能在下面增加cookie
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

        for cookie in cookies:
            # cookie不支持浮点数，expiry可能会是float，它又不重要，为防报错，可以提前删
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        # 现在再去那个页面，就能登录了 因为cookie信息在里面了
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element_by_css_selector(".index_service_cnt_itemWrap:nth-child(2)").click()

        self.driver.find_element_by_id("js_upload_file_input").send_keys("C:/Users/lynno/OneDrive/Desktop/霍格沃茨笔记.xlsx")
        # 拿到文本属性，然后进行断言，判断上传的文档是不是 “霍格沃茨笔记.xlsx”
        assert "霍格沃茨笔记.xlsx" == self.driver.find_element_by_id("upload_file_name").text
        sleep(3)