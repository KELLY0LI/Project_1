# coding=utf-8

'''
Kelly 20170903
《Selenium2 自动化测试实战 基于Python语言》
P218 例子
'''
import os

result_dir = os.getcwd() + '\\report'

lists = os.listdir(result_dir)

#按时间排序 getmtime
lists.sort(key=lambda fn: os.path.getmtime(result_dir + "\\" + fn))

print(('最新的文件是： ' + lists[-1]))
