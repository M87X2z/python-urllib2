# coding:utf-8
import bs4
import re
from bs4 import BeautifulSoup

# 二、网页解析器：用于从网页中提取出有价值数据的工具
# Python的几种网页解析器：正则表达式、python自带的html.parser、第三方库BeautifulSoup/lxml

# 验证bs4是否安装
print bs4

# bs4如何工作？
# html网页 ---->
# 创建beautifulsoup对象 ---->
# 搜索节点元素find_all、find(可按照节点的名称、属性以及文字来搜索) ---->
# 访问节点元素的名称、属性以及文字.

# 根据html网页字符串内容创建BeautifulSoup对象
docs = "<html>" \
         "<body>" \
         "<a href='1.html' class='bs'>python</a>" \
         "<a href='2.html' class='bs'>java</a>" \
         "<p class='cont'>编程语言</p>" \
         "</body>" \
         "</html>"
soup = BeautifulSoup(
    docs,
    'html.parser',
    from_encoding='utf-8'
)

# 搜索节点
print '获取所有的链接：'
links = soup.find_all('a')
for link in links:
    print link.name, link['href'], link.get_text()

print '普通方式搜索节点：'
linkNode = soup.find('a', href='1.html')
print linkNode.name, linkNode['href'], linkNode.get_text()

print '正则匹配方式搜索节点：'
inks = soup.find_all('a', href=re.compile('html'))
for link in inks:
    print link.name, link['href'], link.get_text()

print '获取p段落的文字内容：'
pContent = soup.find('p', class_='cont')
print pContent.name, pContent.get_text()
