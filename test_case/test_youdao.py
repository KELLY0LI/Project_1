# -*- coding:utf-8 -*-

'''
Kelly 20170901/20170903
《Selenium2 自动化测试实战 基于Python语言》
P201 P209 test_youdao.py
'''

from selenium import webdriver
from models import sdriver
import unittest
import time

class Youdao(unittest.TestCase):
    """有道字典测试"""

    def setUp(self):
        self.driver = sdriver.browser('firefox')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.base_url = "http://www.youdao.com"

    def tearDown(self):
        self.driver.quit()
        print("test_youdao end")
        
    def test_youdao(self):
        '''搜索关键词：webdriver'''
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_name("q").clear()
        driver.find_element_by_name("q").send_keys("webdriver")
        driver.find_element_by_xpath('//*[@id="form"]/button').click()
        time.sleep(2)
        title = driver.title
        self.assertEqual(title, "【webdriver】什么意思_英语webdriver的翻译_音标_读音_用法_例句_在线翻译_有道词典")


if __name__ == "__main__":
    unittest.main()
