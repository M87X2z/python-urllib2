# coding:utf-8
import url_manager, html_downloader, html_parser, html_outputer, datetime, urlparse as up

# 爬虫深度定义
maxDeep = 100

class SpiderMain(object):
    def __init__(self):
        self.datas = []
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        self.urls.add_new_url(root_url)
        count = 1
        while self.urls.has_new_url():
            # 针对无效url需要数据异常处理
            new_url = self.urls.get_new_url()
            # noinspection PyBroadException
            try:
                print 'craw %d : %s' % (count, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(self, new_data)

                # 终止爬取条件
                if count == maxDeep:
                    break
            except BaseException as be:
                print be.message
                print 'craw failed at %s' % new_url
            # 计数
            count += 1
        self.outputer.output_html(self)


if __name__ == '__main__':
    url = 'https://baike.baidu.com/item/Python/407313'
    obj_spider = SpiderMain()
    s_time = datetime.datetime.now()
    obj_spider.craw(url)
    e_time = datetime.datetime.now()
    print '预设爬虫 %d 条百科数据，总耗时(秒)：%d' % (maxDeep, (e_time - s_time).seconds)