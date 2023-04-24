 # comicup29-ticket-buy

cp29门票购买脚本，支持Bilibili会员购及ALLCPP，修改一下也可以去买别的东西

脚本不是很完善，只是为了方便购买，在使用时根据自己需求修改，发现问题可以发isssue或者修复发pr，阿里嘎多~

本脚本仅供学习交流使用，不得用于商业用途，如有侵权请联系删除

## 如何使用

1. 下载该项目ZIP文件 https://github.com/Hobr/comicup29-ticket-buy （Code->Download ZIP）并解压得到文件夹“comicup29-ticket-buy-main” 双击进入文件夹目录
2. 安装Python 打开https://www.python.org/downloads/ ，然后点击黄色按钮下载Python
3. 安装时选中“Add Python to PATH”紧接着点击“Customize installation”确保勾选所有可选项后 “Next”
4. 打开终端（Cmd或者Powershell）输入命令 pip config set global.index-url https://mirrors.ustc.edu.cn/pypi/web/simple & pip install -r requirements.txt
5. 检查您使用的浏览器版本 （打开设置->关于来检查您的浏览器版本）
6. 下载与您的浏览器版本匹配的Web驱动程序版本
> - Chrome	ChromeDriver	https://chromedriver.chromium.org/downloads
> - Internet Explorer	Internet Explorer Driver Server	https://www.selenium.dev/documentation/ie_driver_server/
> - Microsoft Edge	Microsoft Edge Driver	https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
> - Firefox	GeckoDriver	https://github.com/mozilla/geckodriver/releases
> - Opera	OperaChromiumDriver	https://github.com/operasoftware/operachromiumdriver/releases
7. 解压Web驱动程序得到“.exe”文件
8. 将“.exe”文件放在安装好的Python目录的Scripts文件夹内
9. 该项目默认Web驱动程序为Chrome  如果你用的不是Chrome 请用记事本分别打开 “bilibili.py”和“cpp.py” 将Chrome改为你使用的浏览器 （以Microsoft Edge为例 请将“.py”文件中的所有“Chrome”改成“Edge”）
10. 改完后 在刚刚打开的cmd窗口内输入指令python .\bilibili.py或者python .\cpp.py
11. 根据要求输入yes 在网页登陆完成后 回到cmd输入任意字符 回车 成功获取Cookies
12. 再次输入指令python .\bilibili.py或者python .\cpp.py 即可开始抢票

## 补充
1. 可以通过设置“config.json”文件中的"send_email": <false/true>,来选择是否启用发送QQ邮件功能
2. 默认是购买Day1普票 可以修改“.py”文件中的'2023-05-02 周二'或'DAY1 普通票'
