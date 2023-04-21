from selenium.webdriver.common.by import By
from selenium import webdriver

cookies = []

WebDriver = webdriver.Chrome()
WebDriver.get("https://show.bilibili.com/platform/detail.html?id=72320")
print("进入购票页面成功")
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

while True:
    try:
        ticket = WebDriver.find_element(By.XPATH, "//*[@id='app']/div[2]/div[2]/div[2]/div[4]/ul[1]/li[2]/div[1]") # 最后一项[]对应票的类型
        if ticket.get_attribute('class') == 'selectable-option unable':
            print("无票")
            raise
        ticket.click()
        WebDriver.find_element(By.CLASS_NAME, "product-buy.enable").click()
    except:
        print("无法购买")
        WebDriver.refresh();
        continue

    try:
        WebDriver.find_element(By.CLASS_NAME, "check-icon").click()
        WebDriver.find_element(By.CLASS_NAME, "confirm-paybtn.active").click()
        print("订单创建完成")
    except:
        print("无法点击创建订单")
        continue
