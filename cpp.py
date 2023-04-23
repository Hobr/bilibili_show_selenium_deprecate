from selenium.webdriver.common.by import By
from selenium import webdriver
from utils import EmailHelper
import json
import random
import time

# 加载配置文件
with open('./config.json', 'r') as f:
    config = json.load(f)

# 检查cookie
if len(config["ccp_cookies"]) == 0:
    print("cookies未设置, 是否进行cookies获取?(手动登录后回到终端按任意键,程序将自动获取cookies)")
    getcookies = input("输入yes开始获取cookies:")
    if getcookies == "yes":
        WebDriver = webdriver.Chrome()
        WebDriver.get("https://cp.allcpp.cn/#/ticket/detail?event=1074")
        print('=============================================')
        input("登录完成后请按任意键继续\n")
        config["ccp_cookies"] = WebDriver.get_cookies()
        with open('./config.json', 'w') as f:
            json.dump(config, f, indent=4)
        print("cookies 保存好啦,在运行一次脚本吧")
        exit(0)
    else:
        print("未输入 yes, 程序结束")
        exit(1)

WebDriver = webdriver.Chrome()
WebDriver.get("https://cp.allcpp.cn/#/ticket/detail?event=1074")
print("进入购票页面成功")
for cookie in config["ccp_cookies"]:
    WebDriver.add_cookie(
        {
            'domain': cookie['domain'],
            'name': cookie['name'],
            'value': cookie['value'],
            'path': cookie['path']
        }
    )
WebDriver.get("https://cp.allcpp.cn/#/ticket/detail?event=1074")

if config["send_email"]:
    email_helper = EmailHelper(config["qq_email_config"])
while True:
    time.sleep(random.uniform(0.1, 1))
    currurl = WebDriver.current_url
    if "cp.allcpp.cn/#/ticket/detail" in currurl:
        try:
            ticket = WebDriver.find_element(
                By.XPATH, "//*[@id='root']/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div[text()='DAY1 普通票']")  # 最后一项[]对应票的类型
            ticket.click()
            if ticket.get_attribute('class') == 'ticket-box disabled':
                print("无票")
                WebDriver.refresh()
                continue
            WebDriver.find_element(
                By.XPATH, "//*[@id='root']/div/div[2]/div/div/div[1]/div/div[2]/div[2]/button").click()
        except:
            print("无法购买")
            WebDriver.refresh()
    elif "cp.allcpp.cn/#/ticket/confirmOrder" in currurl:
        try:
            WebDriver.find_element(By.CLASS_NAME, "purchaser-info").click()
            WebDriver.find_element(
                By.XPATH, "//*[@id='root']/div/div[2]/div/div/button").click()
            print("下单中")
            if config["send_email"]:
                try:
                    email_helper.try_send_email()
                except:
                    print("邮件发送失败")
        except:
            print("无法点击创建订单")
