"""
功能描述：
编写人：SongXuwen
编写日期：
实现逻辑：
    1.
    2.
    3.

"""
'''
发送普通邮件
一、配置邮箱属性
二、组装邮件内容和标题
三、登录并发送邮件
'''
# import smtplib,time,os
# from email.mime.text import MIMEText
# from email.header import Header
#
# class SendEmail():
#     def sendamail(self):
#         # 一、配置邮箱属性
#         # 发送邮箱
#         sender = 'xuwen0525@163.com'
#         # 收件邮箱
#         receiver = '376879307@qq.com'
#         # 发送邮件主题
#         t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#         subject = '自动化测试结果' + t
#         # 发送邮件服务器
#         smtpserver = 'smtp.163.com'
#         # 发送邮箱用户/密码,可以使用授权码或者密码
#         username = 'xuwen0525'
#         passerword = 'XGYFSGGTPEUEKHCR'
#         # 邮件内容
#         content = 'Python 邮件发送测试'
#
#         # 二、组装邮件内容和标题
#         msg = MIMEText(content, 'plain', 'utf-8')
#         msg['Subject'] = subject
#         msg['From'] = sender
#         msg['To'] = receiver
#
#         # 三、登录并发送邮件
#         try:
#         # 1.实例化smtp类
#             s = smtplib.SMTP()
#             # 2.连接smtp服务器
#             s.connect(smtpserver)
#             # 3.登录邮箱
#             s.login(username, passerword)
#             # 4.设置发件人，收件人，邮件内容
#             s.sendmail(sender, receiver, msg.as_string())
#         except Exception as msg:
#             print(f'邮件发送失败，{msg}')
#         else:
#             print('邮件发送成功')
#         finally:
#             s.quit()
#
# if __name__ == '__main__':
#     a = SendEmail()
#     a.sendamail()

'''
发送带html附件的邮件
1、配置邮箱属性
2、增加附件，组装邮件内容和标题
3、登录并发送邮箱

'''
import smtplib,time,os
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

class SendHtmlEmail():
    def send_html_email(self):
        sender = 'xuwen0525@163.com'
        receiver = '376879307@qq.com'
        t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        subject = '带html的自动化测试结果' + t
        smtpserver = 'smtp.163.com'
        username = 'xuwen0525'
        passerword = 'XGYFSGGTPEUEKHCR'

        file = 'result.html'
        with open(file, 'rb') as f:
            mail_body = f.read()
            msg = MIMEMultipart()
            att = MIMEText(mail_body, 'plain', 'utf-8')
            att['Content-Type'] = 'application/octet-stream'
            att['Content-Disposition'] = 'attachment; filename=report.html'
            msg.attach(att)

            content = '自动化测试报告详情，请查收附件'
            msg.attach(MIMEText(content, 'plain', 'utf-8'))
            msg['subject'] = subject
            msg['From'] = sender
            msg['To'] = receiver

        try:
            smtp = smtplib.SMTP()
            smtp.connect(smtpserver)
            smtp.login(username, passerword)
            smtp.sendmail(sender, receiver, msg.as_string())
        except Exception as msg:
            print(f'邮件发送失败，失败原因{msg}')
        else:
            print('邮件发送成功')
        finally:
            smtp.close()
        

if __name__ == '__main__':
    a = SendHtmlEmail()
    a.send_html_email()