# -*- coding:utf-8 -*-

'''
Kelly 20170911
《Selenium2 自动化测试实战 基于Python语言》
P281
定义driver路径，防止Jenkins调用引起的出错
'''

from selenium import webdriver
import os

def browser(browserName):
    '''
    :param browserName: chrome or Ie or firefox
    :return: driver
    '''

    dirdriver = r"C:\pydriver"

    if browserName == 'chrome':
        pathchrome = dirdriver + "\\chromedriver.exe"
        driver = webdriver.Chrome(executable_path = pathchrome)
    elif browserName == 'Ie':
        pathie = dirdriver + "\\IEDriverServer.exe"
        driver = webdriver.Ie(executable_path = pathie)
    else:
        pathff = dirdriver + "\\geckodriver.exe"
        driver = webdriver.Firefox(executable_path = pathff)
    return driver

if __name__ == '__main__':
    dr = browser('chrome')
    dr.get("http://www.baidu.com")
    print("Run OK")
    dr.quit()
