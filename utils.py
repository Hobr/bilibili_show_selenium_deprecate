def send_qq_email(sender, password, receiver):
    import smtplib
    from email.mime.text import MIMEText

    # 发送到服务器的文本信息
    subject = '脚本运行结果'
    content = '抢到票啦,请在规定时间内支付'
    msg = MIMEText(content)

    # msg['Subject']是发送邮件的主题
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    # 发送邮件时qq邮箱，对应qq邮箱服务器域名时smtp.qq.com  对应端口时465
    with smtplib.SMTP_SSL(host='smtp.qq.com', port=465) as server:
        # 登录发送者的邮箱
        server.login(sender, password)

        # 开始发送邮件
        server.sendmail(sender, receiver, msg.as_string())
        print("Successfully sent email")
