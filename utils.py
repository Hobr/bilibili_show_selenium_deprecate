import smtplib
from email.mime.text import MIMEText
import time

class EmailHelper:
    def __init__(self, email_config):
        self.last_send_time = 0
        self.sender = email_config["sender"]
        self.password = email_config["password"]
        self.receiver = email_config["receiver"]
        pass
    def try_send_email(self):
        # 防止连续发送邮件
        if (int(time.time()) - self.last_send_time < 60*3):
            return

        # 发送到服务器的文本信息
        subject = '脚本运行结果'
        content = '检测到有余票,已进行下单,请确认'
        msg = MIMEText(content)

        # msg['Subject']是发送邮件的主题
        msg['Subject'] = subject
        msg['From'] = self.sender
        msg['To'] = self.receiver

        # 发送邮件时qq邮箱，对应qq邮箱服务器域名时smtp.qq.com  对应端口时465
        with smtplib.SMTP_SSL(host='smtp.qq.com', port=465) as server:
            # 登录发送者的邮箱
            server.login(self.sender, self.password)

            # 开始发送邮件
            server.sendmail(self.sender, self.receiver, msg.as_string())
            print("Successfully sent email")
        # 保存发件时间
        self.last_send_time = int(time.time())
