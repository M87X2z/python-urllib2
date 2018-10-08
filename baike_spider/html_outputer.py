# coding:utf-8

class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    # 搜集价值数据
    @staticmethod
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    # 将搜集到的价值数据输出到html中
    @staticmethod
    def output_html(self):
        fout = open('output.html', 'w')
        fout.write('<html>')
        fout.write('<head>')
        fout.write('<meta charset="UTF-8">')
        fout.write('</head>')
        fout.write('<body>')
        fout.write('<table border="1">')

        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['title'].encode('utf-8'))
            fout.write('<td>%s</td>' % data['summary'].encode('utf-8'))
            fout.write('</tr>')

        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
        fout.close()