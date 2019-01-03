# coding:utf-8
# 定义空字典
a = {}
b={}
print(type(a))
# 向字典中添加元素
a['a']=1
print(a)
# 把字典a中的键值对更新到b中
b.update(a)
print(b)
# 将字典元素以列表形式输出
print(a.items())
# 添加字典中某个key的默认值，如果该key不存在，则输出默认值
a.setdefault('b',2)
a.setdefault('a',2)
print(a)
# 按照key值输出value
print(a.get('b'))
# 按照key值输出value，如果key不存在则输出设置的默认值
print(a.get('f',6))
# 删除字典中key的值
a.pop('a')
print(a)
# 以列表形式输出字典中的key值
print(a.keys())
# 以列表形式输出字典中的value值
print(a.values())
#清除字典中的所有元素
a.clear()
print(a)
# 创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值
l01=['a','b','c']
l02=[1,2,3]
c={}.fromkeys(l01,3)
print(c)

# 练习  计算所有人每科的平均分，以及每人成绩的平均分
fenshu = {
    'xiaowang': {
        'shuxue': 99,
        'yuwen': 60,
        'yingyu': 78
    },
    'xiaoming':{
        'shuxue': 75,
        'yuwen': 88,
        'yingyu': 93
    },
    'xiaolei': {
        'shuxue': 70,
        'yuwen': 68,
        'yingyu': 65
    },
    'xaiofang': {
        'shuxue': 98,
        'yuwen': 96,
        'yingyu': 89
    },
}
print(fenshu.keys())
print(fenshu.values())
course=['shuxue','yuwen','yingyu']
#求每个学生的平均分数
for k in fenshu.keys():
    sum = 0
    for c in course:
        sum=sum+fenshu[k][c]
        print(sum)
    print("学生{0}的平均成绩是{1}".format(k,  sum/3))

#求所有学生每科的平均分数
for c in course:
    sum = 0
    for k in fenshu.keys():
        sum=sum+fenshu[k][c]
        print(sum)
    print("科目{0}的平均成绩是{1}".format(c,  sum/4))



#统计文件中的每个单词的个数
file=open('/Users/shogakusha/PycharmProjects/20181104/lesson02/word.txt','r')
# list=file.read().split('\n')
# file.close()
# print(list)
# list_final=[]
# for i in list:
#     if i=='':
#         list = list.remove('')
#     f = i.split(' ')
#     print(f)
#     for s in f:
#         if s == '--':
#             f.remove(s)
#         else:
#             for x in [',', '.', '-', '*', '!']:
#                 if s.find(x):
#                     s = s.replace(x, '',2)
#         list_final.append(s.lower())
# print(list_final)
# for n in list_final:
#     count=list_final.count(n)
#     print('单词{0}共有{1}个'.format(n, count))
content = file.read()
file.close()
content = content.replace(".","")
content = content.replace("--","")
content = content.replace("*","")
content = content.replace(",","")
content = content.replace("!","")
lines = content.split('\n')

dic = {}
for line in lines:
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in dic:
            dic.setdefault(word, 1)
        else:
            dic[word] += 1
        # if dic.get(word):
        #     dic[word] += 1
        # else:
        #     dic[word] = 1
print(dic)
