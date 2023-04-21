import time
from selenium.webdriver.common.by import By
from selenium import webdriver

# 你的cookie
cookies = []

WebDriver = webdriver.Chrome()
# 购票页面
WebDriver.get("https://show.bilibili.com/platform/detail.html?id=72320")
time.sleep(1)
print("进入购票页面成功")
time.sleep(1)
for cookie in cookies:
    WebDriver.add_cookie(
    {
        'domain':cookie['domain'],
        'name': cookie['name'],
        'value':cookie['value'],
        'path': cookie['path']
    }
)
WebDriver.refresh()
time.sleep(1)

while True:
    try:
        WebDriver.find_element(By.CLASS_NAME, "product-buy.enable").click()
        time.sleep(1)
        print("进入购买页面成功")
    except:
        print("无法购买")
        WebDriver.refresh();

    try:
        WebDriver.find_element(By.CLASS_NAME, "check-icon").click()
        time.sleep(1)
        WebDriver.find_element(By.CLASS_NAME, "confirm-paybtn.active").click()
        print("订单创建完成")
    except:
        print("无法点击创建订单")
