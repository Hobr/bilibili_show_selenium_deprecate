from selenium.webdriver.common.by import By
from selenium import webdriver
import json
import random
import time

day1Token = "cAARqAAAHu6gEAAQAFz_g."
day2Token = "cAARqAAAHu6wEAAQAF0Ag."

# 配置载入
with open("./config.json", "r") as f:
    config = json.load(f)

# 初始化
if config["init"] == 0:
    print("第一次使用需要配置一下!\n")
    WebDriver = webdriver.Chrome()
    WebDriver.get(config["studyUrl"])
    print("首先请动手登录一下B站\n")
    WebDriver.find_element(By.CLASS_NAME, "nav-header-register").click()
    input("登录完成后请按任意键继续\n")
    config["cookie"] = WebDriver.get_cookies()
    print("cookie已保存")
    WebDriver.quit()
    config["day"] = int(input("你想抢Day几的票?只输入数字1或2!\n"))
    config["init"] = 1
    with open("./config.json", "w") as f:
        json.dump(config, f, indent=4)

# WebDriver初始化
WebDriver = webdriver.Chrome()
WebDriver.get(config["studyUrl"])

# 载入Cookie
for cookie in config["cookie"]:
    WebDriver.add_cookie({
        "domain": cookie["domain"],
        "name": cookie["name"],
        "value": cookie["value"],
        "path": cookie["path"]
    })

if config["day"] == 1:
    afterToken = day1Token
elif config["day"] == 2:
    afterToken = day2Token

# 时间戳获取
if len(config["currentToken"]) == 0:
    print("获取时间戳中")
    WebDriver.get(config["studyUrl"])
    WebDriver.find_element(By.CLASS_NAME, "product-buy.enable").click()
    time.sleep(3)
    config["currentToken"] = WebDriver.current_url[59:65]
    config["actualUrl"] = "https://show.bilibili.com/platform/confirmOrder.html?token=" + \
        config["currentToken"] + afterToken
    with open("./config.json", "w") as f:
        json.dump(config, f, indent=4)

# 下单页面
config["actualUrl"] = "https://show.bilibili.com/platform/confirmOrder.html?token=" + \
    config["currentToken"] + afterToken
WebDriver.get(config["actualUrl"])

# 持续下单
while True:
    time.sleep(random.uniform(0.6, 1.2))
    try:
        try:
            WebDriver.find_element(By.CLASS_NAME,
                                   "confirm-paybtn.active").click()
            print("运行中")
        except BaseException:
            if WebDriver.find_element(
                    By.XPATH,
                    "//*[@id='app']/div[2]/div/div[5]/div/div[2]/div/div[2]/div"
            ).text == "当前页面已失效，请返回详情页重新下单":
                print("时间戳已过期,获取时间戳中")
                WebDriver.get(config["studyUrl"])
                WebDriver.find_element(By.CLASS_NAME,
                                       "product-buy.enable").click()
                time.sleep(3)
                config["currentToken"] = WebDriver.current_url[59:65]
                config["actualUrl"] = "https://show.bilibili.com/platform/confirmOrder.html?token=" + \
                    config["currentToken"] + afterToken
                WebDriver.get(config["actualUrl"])
                with open("./config.json", "w") as f:
                    json.dump(config, f, indent=4)
    except Exception as e:
        try:
            if WebDriver.find_element(
                    By.XPATH,
                    "//*[@id='app']/div[2]/div/div[7]/div/h1").text == "扫码支付":
                print("已下单,请手动支付")
                WebDriver.quit()
                exit(0)
        except BaseException:
            print(e)
            WebDriver.find_element(By.CLASS_NAME, "check-icon").click()
            print("无法创建订单")
            WebDriver.refresh()
