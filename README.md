# comicup29-ticket-buy

cp29门票购买脚本，支持Bilibili会员购及ALLCPP，修改一下也可以去买别的东西

脚本不是很完善，只是为了方便购买，在使用时根据自己需求修改

本脚本仅供学习交流使用，不得用于商业用途，如有侵权请联系删除

## 如何使用

1. 安装Python
2. 安装selenium：`pip install -r requirements.txt`
3. 默认是购买Day1普票，可以修改find_element(By.XPATH....div[第几个])，第几个对应网页中的选项顺序
4. 提前在平台内填写实名信息
5. 设置config.json文件,是否发送qq邮件以及邮件信息(sender->发件邮箱, password->发件邮箱授权码, receiver->收件邮箱)
6. 运行脚本，根据命令行提示获取cookie
7. 再次运行，开始抢票
