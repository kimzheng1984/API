# coding:utf-8

import unittest
from HTMLTestRunner import HTMLTestRunner
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time
import os
from File_remove import reports_removed
from File_remove import results_removed
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


# 定义发送邮件
def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    # 发送邮箱服务器
    smtpserver = 'smtp.mxhichina.com'
    # 发送邮箱用户名/密码
    user = 'kim.zheng@91nuanyou.com'
    password = 'xiaozheng_1829'
    # 发送邮箱
    sender = 'kim.zheng@91nuanyou.com'
    # 接收邮箱
    receiver = 'kim.zheng@91nuanyou.com'
    # receiver = ['siounex@91nuanyou.com', 'jerry@91nuanyou.com', 'kim.zheng@91nuanyou.com', 'eric.xie@91nuanyou.com', 'vincent@91nuanyou.com', 'steven@91nuanyou.com']
    # 发送主题
    subject = '商户通2.0 API测试报告'

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = receiver
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print ('email has send out!')


# 查找测试报告目录，找到最新的生成的测试报告文件
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport, lists[-1])
    print (file_new)
    return file_new


if __name__ == '__main__':
    test_dir = 'C:\\WORK\\workspace\\python\\shanghutong20_API\\test_case\\'
    test_report = 'C:\\WORK\\workspace\\python\\shanghutong20_API\\report\\'
    report = reports_removed()
    results = results_removed()

    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    filename = test_report + "\\" + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title=u'商户通2.0 API测试报告',
                            description=u'测试概况：如下')
    runner.run(discover)
    fp.close()
    new_report = new_report(test_report)
    send_mail(new_report)

# msg = MIMEText('<html><h1>hello</h1></html>', 'html', 'utf-8')
# msg['subject'] = Header(subject, 'utf-8')
