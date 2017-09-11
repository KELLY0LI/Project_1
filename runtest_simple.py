# -*- coding:utf-8 -*-
'''
Kelly 20170829 / 20170903
《Selenium2 自动化测试实战 基于Python语言》
P200 P213 引用P187
'''
import unittest
import time
from HTMLTestRunner3 import HTMLTestRunner

test_dir = './test_case'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == '__main__':

    now = time.strftime("%Y%m%d_%H%M%S")
    filename = './report/' + now + 'result.html'
    
    #定义报告存放路径
    fp = open(filename, 'wb')

    #定义测试报告
    runner = HTMLTestRunner(stream=fp,
                            title=u'网页搜索自动化测试报告',
                            description=u'用例执行情况: ')
    #运行测试用例
    runner.run(discover)

    #关闭报告文件
    fp.close()



