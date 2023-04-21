from selenium.webdriver.common.by import By
from selenium import webdriver

cookies = []

WebDriver = webdriver.Chrome()
WebDriver.get("https://cp.allcpp.cn/#/ticket/detail?event=1074")
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
WebDriver.get("https://cp.allcpp.cn/#/ticket/detail?event=1074")

while True:
    try:
        ticket = WebDriver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div[3]") # 最后一项[]对应票的类型
        if ticket.get_attribute('class') == 'ticket-box disabled':
            print("无票")
            raise
        ticket.click()
        WebDriver.find_element(By.CLASS_NAME, "sc-idXgbr.bmeITR").click()
    except:
        print("无法购买")
        WebDriver.refresh();
        continue

    try:
        WebDriver.find_element(By.CLASS_NAME, "purchaser-info").click()
        WebDriver.find_element(By.CLASS_NAME, "sc-idXgbr.jfzLdX").click()
        print("订单创建完成")
    except:
        print("无法点击创建订单")
        continue
