# -*- coding:utf-8 -*-
'''
Kelly 20170904
《Selenium2 自动化测试实战 基于Python语言》
P219

project folder
|---report folder
|---test_case folder
|runtest.py

'''
import unittest
import time
import smtplib
import os
from HTMLTestRunner3 import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header

#========setting mail==============
def send_mail(file_new):
    '''发送邮件'''

    f = open(file_new, 'rb')
    mail_body = f.read()      #邮件正文使用最新的测试报告
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header("自动化测试报告", 'utf-8')

    smtpserver = 'smtp.qq.com'
    user = '247219667@qq.com'
    password = 'thyqavdubypibghe'
    sender = '247219667@qq.com'
    receiver = ['ling-yan.li@hpe.com']

    #连接发送 含端口号
    try:
        smtp = smtplib.SMTP_SSL(smtpserver, 465)
        smtp.connect(smtpserver)
        smtp.login(user, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        print("邮件发送成功")
    except BaseException as err:
        print("邮件发送失败，错误为: \n", err)
    finally:
        smtp.quit()

#========find newest report==============
def newest_report(testreport):
    '''找到最新生成的测试报告'''
    
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport +"\\"+ fn))
    file_new = os.path.join(testreport, lists[-1])
    return file_new

if __name__ == '__main__':
    case_dir = os.getcwd() + '\\test_case'
    report_dir = os.getcwd() + '\\report'

    discover = unittest.defaultTestLoader.discover(case_dir, pattern='test*.py')

    now = time.strftime("%Y%m%d_%H%M%S")
    filename = './report/' + now + 'result.html'
    
    #定义报告存放路径
    fp = open(filename, 'wb')

    #定义测试报告
    runner = HTMLTestRunner(stream=fp,
                            title=u'自动化测试报告',
                            description=u'用例执行情况: ')
    #运行测试用例
    runner.run(discover)

    #关闭报告文件
    fp.close()

    newest_report = newest_report(report_dir)
    send_mail(newest_report)
