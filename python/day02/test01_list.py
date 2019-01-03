# coding:utf-8
a = [0,1]
print(type(a))
# 添加元素到列表中
a.append(2)
print(a)
# 将元素插入列表的指定位置
a.insert(0,3)
print(a)
#输出列表中指定元素的个数
print(a.count(2))
#输出列表中指定元素的索引值
print(a.index(3))
#删除列表中指定位置的元素并输出
print(a.pop(1))
print(a)
#排序
a.sort()
#反转
a.reverse()
print(a)
print(a.pop(1))
#删除列表中的某一个元素值
a.remove(3)
print(a)

# 练习列表去重
a = [1, 2, 3, 4, 2, 5, 6, 4, 7, 2, 1]
c = []
for i in a:
    if i in c:
        continue
    else:
        c.append(i)
print(c)
# print(list(set(a)))

print(a+c)

# 冒泡排序
data = [3, 1, 7, 6, 2, 9, 4, 5, 8]
l = len(data)
for d in range(l):
    for q in range(l-1):
        if data[q] > data[q+1]:
            data[q], data[q+1] = data[q+1], data[q]
print(data)
# data.sort()
