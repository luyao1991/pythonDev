# coding:utf-8
# 生成器
# 生成一个列表
a=[i for i in range(10)]
print(a)
# 生成一组
b=[(x,y) for x in range(5) for y in range(6) if x != y]
print(b)
# 按照指定位数进行四舍五入
pi=3.14159265
c = [str(round(pi, 3)) for i in range(1, 6)]
print(c)
# 输出一组二维列表的相同索引位置的值
matrix=[[1,2,3],[3,4,5],[0,6,5]]
d = [[row[i] for row in matrix] for i in range(2)]
print(d)
# 生成一组字典
e={x: x**2 for x in (2, 4, 6)}
print(e)


