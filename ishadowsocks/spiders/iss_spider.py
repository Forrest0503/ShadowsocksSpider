#coding=utf-8
# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")

from scrapy.spider import Spider
from scrapy.selector import Selector
from ishadowsocks.items import IssItem
from biplist import *
import plistlib
import base64
import os

USERNAME = 'Jason'

class IssSpider(Spider):
    name = "ishadowsocks"
    allowed_domains = ["ishadowsocks.org"]
    start_urls = [
    "http://www.ishadowsocks.org",
    ]

    def parse(self, response):
        sectionA = response.xpath('//section[@id="free"]/div[@class="container"]/div[@class="row"]/div[@class="col-lg-4 text-center"]')[0]

        item = IssItem()
        item['server'] = sectionA.xpath('h4/text()').extract()[0].split(":")[1]
        item['port'] = sectionA.xpath('h4/text()').extract()[1].split(":")[1]
        item['password'] = sectionA.xpath('h4/text()').extract()[2].split(":")[1]
        item['method'] = sectionA.xpath('h4/text()').extract()[3].split(":")[1]

        #生成plist
        plistGenerator = PlistGenerator()
        stringPlist = plistGenerator.parse(str(item['password']))
        print(stringPlist)
        plistGenerator.generate(stringPlist)
        #更新系统plist
        os.system('defaults import clowwindy.ShadowsocksX result.plist')
        #杀死进程
        os.system('killall ShadowsocksX')
        #重启进程
        os.system('open /Applications/ShadowsocksX.app')
        return item

class PlistGenerator():
    def generate(self, plist):
        try:
            writePlist(plist, "result.plist")
        except (InvalidPlistException, NotBinaryPlistException), e:
            print "Something bad happened:", e

    def parse(self, password):
        try:
            plist = readPlist("/Users/" + USERNAME + "/Library/Preferences/clowwindy.ShadowsocksX.plist")
            oldConfig = plist["config"]
            p_index = oldConfig.find('","method":"aes-256-cfb","server_port":443,"remarks":"","server":"US1.ISS.TF"')
            if p_index != -1:
                newConfig = oldConfig[:p_index-8] + password + oldConfig[p_index:]
                plist["config"] = Data(newConfig)
                plist["proxy password"] = password
                plist["proxy ip"] = "US1.ISS.TF"
                return plist
            else:
                print("Error1")
        except (InvalidPlistException, NotBinaryPlistException), e:
            print "Not a plist:", e



