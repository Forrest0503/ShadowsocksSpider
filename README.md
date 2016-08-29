# ShadowsocksSpider
shadowsocks爬虫，从www.ishadowsocks.org爬取数据。

## 使用方法
目前仅支持Mac OS，需要安装Scrapy框架和Shadowsocks for OSX。

**首先，请备份/Users/XXX/Library/Preferences/clowwindy.ShadowsocksX.plist**
要恢复配置文件，执行

`defaults import clowwindy.ShadowsocksX /path/to/yyy.plist`

方法一：

0. 安装Scrapy框架和ShadowsocksX

`pip install scrapy`
> ShadowsocksX:
> https://github.com/shadowsocks/shadowsocks-iOS/wiki/Shadowsocks-for-OSX-帮助

1. 下载后将ishadowsocks文件夹放入任意目录

2. 打开Terminal，进入ishadowsocks目录，执行

 `scrapy crawl ishadowsocks`

方法二：
配合Alfred Workflow食用更酸爽~

1. 下载后将ishadowsocks文件夹放入系统主目录（可以放在任意位置，但要相应的修改workflow）
2. 安装ishadowsocks文件夹中的workflow
3. 打开Alfred2 输入ss 回车即可


