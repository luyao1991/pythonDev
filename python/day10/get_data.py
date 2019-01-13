# coding:utf-8
# @File:  get_data.py
# @Author:  guozhiwen
# @Date:  2019/1/13
# @Time:  10:05 AM
# @Version:  v3.6.4
import json
import time

class GetData:
    NUM = 10

    def __init__(self):
        self.results = self.load_resource("/Users/shogakusha/Workspaces/github/pythonDev/python/day10/static/data.json")

    def get(self, page):
        url = 'https://v2.sohu.com/'
        data = self.results[page * GetData.NUM: (page + 1) * GetData.NUM - 1]
        for d in data:
            d['url'] = url + d['url']
            if 'images' in d and d['images']:
                d['image'] = d['images'][0]
            t = time.localtime(d['publicTime'] / 1000)
            d['publicTime'] = time.strftime("%Y-%m-%d %H:%M:%S", t)
        return data

    #  加载json文件数据
    def load_resource(self, file):
        with open(file, 'r', encoding='utf-8') as f:
            lines = list(set(f.readlines()))  # 读取指定行数的数据,并去重
            # print(len(line))
            # lines=list(map(json.loads, lines))
        return list(map(json.loads, lines))  # 利用map进行json批处理生成json数据

    #   筛选数据
    def filter_resource(self, line):
        return line['resourceType'] == 1

    #   按照publicTime进行倒序排列
    def sort(self, lines):
        length = len(lines)
        for i in range(length):
            for j in range(length - 1):
                print(i * length + j)
                if lines[j]['publicTime'] < lines[j + 1]['publicTime']:
                    lines[j], lines[j + 1] = lines[j + 1], lines[j]
        return lines

    # 提取去重后的authorName字段数据
    def extract(self, lines):
        author_name = []
        for i in lines:
            author_name.append(i['authorName'])
        return list(set(author_name))

    #   主函数
    def main(self, file):
        lines = self.load_resource(file)  # 加载后的数据
        results = self.sort(list(filter(self.filter_resource, lines)))  # 将加载的数据进行筛选并排序
        with open('/Users/shogakusha/Workspaces/github/pythonDev/python/day10/static/data.json', 'w',
                  encoding='utf-8') as d:  # 将处理后的数据写入本地data.json文件
            for result in results:
                # print(result['publicTime'])
                d.write(json.dumps(result) + '\n')
        print(self.extract(list(filter(self.filter_resource, lines))))  # 打印提取后的authorName数据


if __name__ == '__main__':
    file = '/Users/shogakusha/Desktop/06-期中考试.json'
    # file = '/Users/shogakusha/Workspaces/github/pythonDev/python/day10/static/data.json'
    news = GetData()
    news.main(file)
