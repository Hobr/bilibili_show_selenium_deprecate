from selenium.webdriver.common.by import By
from selenium import webdriver
from utils import send_qq_email
import json
import random
import time

# 加载配置文件
with open('./config.json', 'r') as f:
    config = json.load(f)

# 检查cookie
if len(config["bilibili_cookies"]) == 0:
    print("cookies未设置, 是否进行cookies获取?(手动登录后回到终端按任意键,程序将自动获取cookies)")
    getcookies = input("输入yes开始获取cookies:")
    if getcookies == "yes":
        WebDriver = webdriver.Edge()
        WebDriver.get("https://show.bilibili.com/platform/detail.html?id=72320")
        print('=============================================')
        input("登录完成后请按任意键继续\n")
        config["bilibili_cookies"] = WebDriver.get_cookies()
        with open('./config.json', 'w') as f:
            json.dump(config, f, indent=4)
        print("cookies 保存好啦,在运行一次脚本吧")
        exit(0)
    else:
        print("未输入 yes, 程序结束")
        exit(1)

WebDriver = webdriver.Edge()
WebDriver.get("https://show.bilibili.com/platform/detail.html?id=72320")
print("进入购票页面成功")
for cookie in config["bilibili_cookies"]:
    WebDriver.add_cookie(
    {
        'domain':cookie['domain'],
        'name': cookie['name'],
        'value':cookie['value'],
        'path': cookie['path']
    }
)
WebDriver.refresh()

while True:
    time.sleep(random.uniform(1, 3))
    currurl = WebDriver.current_url
    if  "show.bilibili.com/platform/detail.html" in currurl:
        try:
            ticket = WebDriver.find_element(By.XPATH, "//*[@id='app']/div[2]/div[2]/div[2]/div[4]/ul[1]/li[2]/div[1]") # 最后一项[]对应票的类型
            ticket.click()
            if ticket.get_attribute('class') == 'selectable-option unable':
                print("无票")
                WebDriver.refresh();
                continue
            WebDriver.find_element(By.CLASS_NAME, "product-buy.enable").click()
        except:
            print("无法购买")
            WebDriver.refresh();
    elif "show.bilibili.com/platform/confirmOrder.html" in currurl:
        try:
            WebDriver.find_element(By.CLASS_NAME, "confirm-paybtn.active").click()
            print("下单中")
            if config["send_email"]:
                email_config = config["qq_email_config"]
                send_qq_email(email_config["sender"], email_config["password"], email_config["receiver"])
            exit(0)
        except:
            print("无法创建订单")
