import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header
from Common.myPie import my_pie  # bug分布图

class Mail:
    def __init__(self):
        # 第三方 SMTP 服务
        self.mail_host = "smtp.qq.com"  # 设置服务器
        self.mail_pass = "xuiattgdleykcach"  # 获取的授权码
        self.sender = '379609962@qq.com'  # 发件人的邮箱地址
        self.receivers = ['cai.panpan@synyi.com','1275372931@qq.com']  # 收件人的邮箱地址，可设置多个


    def send(self):
        # 发送的内容
        content = 'Dear all:\n' \
                  '今日变量中心  V1.4.0.0930  整体进度：进行中【计划  9月30日  发版】\n' \
                  '项目计划如下：\n' \
                  '版本号：V1.4.0.0930\n' \
                  'sit时间为：2021/4/2-2021/4/18\n' \
                  '风险：无\n' \
                  '今日进度：70%\n' \
                      '1、开发已提测7个需求，测试进行中3个需求，详细测试计划详见图表；\n' \
                      '2、BUG总数13个，今日新增：1个，今日关闭：3个，高优先级及以上：1个。\n' \
                  'bug详情：https://redmine.synyi.com/projects/mdm/issues?query_id=2457\n' \
                  '本次需求：https://redmine.synyi.com/projects/mdm/issues?query_id=2398\n' \
                  '占比图：'\


#         content = """
# <p>Python 邮件发送测试...</p>
# <p><a href="http://www.runoob.com">这是一个链接</a></p>
# <p>图片：</p>
# <p><img src="cid:image1"></p>
# """
#         # 指定图片为当前目录
#         fp = open('test.png', 'rb')
#         msgImage = MIMEImage(fp.read())
#         fp.close()
#
#         # 定义图片 ID，在 HTML 文本中引用
#         msgImage.add_header('Content-ID', '<image1>')
#         msgRoot = MIMEMultipart('related')
#         msgRoot.attach(msgImage)



        message = MIMEText(content, 'plain', 'utf-8')

        message['From'] = Header("日报助手", 'utf-8')
        message['To'] = Header(','.join(self.receivers), 'utf-8')

        subject = '测试日报'  # 发送的主题
        message['Subject'] = Header(subject, 'utf-8')
        try:
            smtpObj = smtplib.SMTP_SSL(self.mail_host, 465)
            smtpObj.login(self.sender, self.mail_pass)
            smtpObj.sendmail(self.sender, self.receivers, message.as_string())
            smtpObj.quit()
            print('邮件发送成功')
        except smtplib.SMTPException as e:
            print('邮件发送失败')


if __name__ == '__main__':
    mail = Mail()
    mail.send()