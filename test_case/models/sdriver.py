# -*- coding:utf-8 -*-

'''
Kelly 20170911
《Selenium2 自动化测试实战 基于Python语言》
P281
定义driver路径，防止Jenkins调用引起的出错
'''

from selenium.webdriver import Remote
from selenium import webdriver
import os
import socket

def check_ipport(strIp,intPort):
    '''
    It's to check IP port open or not
    :param strIp: e.g.'127.0.0.1'
    :param intPort: e.g. 4444
    :return: open is True, not open is False
    '''
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((strIp, intPort))
    if result == 0:
        #print("Port is open")
       return True
    else:
        #print("Port is not open")
       return False

def remotebrowser(strbrowserName):
    '''
    It's for remote, hub is 127.0.0.1:4444
    :param browserName: chrome or Ie or firefox
    :return: driver
    '''
    #未启动则启动本机Remote hub
    if not check_ipport('127.0.0.1',4444):
        dircase = os.path.dirname(os.getcwd())
        os.system(dircase +'\\bats\\startuphub.bat')

    if strbrowserName == 'chrome':
        driver = Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                        desired_capabilities={'platform': 'ANY',
                                              'browserName': 'chrome',
                                              'version': '',
                                              'javascriptEnabled': True
                                              }
                        )
    elif strbrowserName == 'firefox':
        driver = Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                        desired_capabilities={'platform': 'ANY',
                                              'browserName': 'firefox',
                                              'version': '',
                                              'javascriptEnabled': True
                                              }
                        )
    else:
        driver = Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                        desired_capabilities={'platform': 'ANY',
                                              'browserName': 'internet explorer',
                                              'version': '',
                                              'javascriptEnabled': True
                                              }
                        )
    return driver

def browser(browserName):
    '''
    :param browserName: chrome or Ie or firefox
    :return: driver
    '''
    dirdriver = os.path.dirname(os.getcwd()) + "\\driver"

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
    dr.quit()
