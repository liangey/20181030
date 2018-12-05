#Author:ley
# --*-- coding: utf-8 --*--
#@Time : 2018-11-02 11:02
#@Author: ley
#@Site : 
#@File : email_learn.py
#@Software : PyCharm

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
my_sender=""
my_pass=""
my_user=""

def mail():
    ret=True
    try:
        msg=MIMEText('填写内容','plain','utf-8')
        msg['From']=formataddr(["发件人昵称",my_sender])
        msg['To']=formataddr(["收件人昵称",my_user])
        msg['Subject']="邮件主题-测试"
        server=smtplib.SMTP_SSL("smtp.qq.com",465)
        server.login(my_sender,my_pass)
        server.sendmail(my_sender,[my_user],msg.as_string())
        server.quit()
    except Exception:
        ret=False
    return ret
ret=mail()
if ret:
    print("发送邮件成功")
else:
    print("发送邮件失败")