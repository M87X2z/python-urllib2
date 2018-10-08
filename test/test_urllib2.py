# coding:utf-8
import urllib2
import cookielib

# 打开网页的三种方法
print '打开爬虫爬取网页的第一种方法：'
url = 'https://www.xinke.org.cn'
mResponse = urllib2.urlopen(url)
print mResponse.getcode()
print len(mResponse.read())

print '========================================='

print '打开爬虫爬取网页的第二种方法：'
mRequest = urllib2.Request(url)
mRequest.add_header('user-agent', 'Mozilla/5.0')
mResponse2 = urllib2.urlopen(mRequest)
print mResponse2.getcode()
print len(mResponse2.read())

print '========================================='

print '打开爬虫爬取网页第三种方法：'
# 创建cookie容器
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
mResponse3 = urllib2.urlopen(url)
print mResponse3.getcode()
print cj
print mResponse3.read()

