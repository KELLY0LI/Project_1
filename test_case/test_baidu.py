# -*- coding:utf-8 -*-

'''
Kelly 20170830/20170903
《Selenium2 自动化测试实战 基于Python语言》
P200 P206 P209 test_baidu.py
'''
import unittest
from selenium import webdriver
import time
from HTMLTestRunner3 import HTMLTestRunner
from models import sdriver
#from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support import expected_conditions as E

class Baidu(unittest.TestCase):
    '''百度搜索测试'''
    def setUp(self):
        self.driver = sdriver.browser('chrome')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.base_url = "http://www.baidu.com"

    def test_baidu(self):
        """搜索关键字: unittest"""
        driver = self.driver
        driver.get(self.base_url)
 #       try:
 #           WebDriverWait(driver, 10).until(EC.title_contains("百度一下"))
 #       except BaseException as errmsg:
 #           print("百度首页未打开" + errmsg)

        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("unittest")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        title = driver.title
        self.assertEqual(title, "unittest_百度搜索")

    def tearDown(self):
        print("test_baidu end")
        self.driver.quit()

if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(Baidu("test_baidu"))

    now = time.strftime("%Y%m%d_%H%M%S")
    filename = '../report/' + now + 'result.html'

    #定义报告存放路径
    fp = open(filename, 'wb')

    #定义测试报告
    runner = HTMLTestRunner(stream=fp,
                            title=u'百度搜索测试报告',
                            description=u'用例执行情况: ')
    #运行测试用例
    runner.run(suite)
    #关闭报告文件
    fp.close()
    
