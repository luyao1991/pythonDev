# coding:utf-8
# nu=0
# while nu<9:
#     nu = nu + 1
#     if nu==7:
#         break
#     else:
#         print("蒙蔽了吧")
#     print(nu)
#
# for i in range(9):
#     print("{0:.2f}".format(i))

# 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和
# m=2
# n=1
# mn=0
# for i in range(20):
#     mn=mn+m/n
#     tmp=m
#     m=tmp+n
#     n=tmp
# print(mn)

#判断是否是回文显示
#方法一
# a=input("输入字符串：")
# b=""
# for i in range(1,len(a)+1):
#     b=b+a[-i]
# print(b)
# if a==b:
#     print("你输入的是回文")
# else:
#     print("你输入的不是回文")
#
# #方法二：
# s = input()
# slen = len(s)
# s1 = s[::-1]
# if s == s1:
#     print("yes")
# else:
#     print("no")


# 有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？

m=[1, 2, 3, 4]
count=0
for i in range(1,5):
    for j in range(1, 5):
        for h in range(1, 5):
            if i==j or j==h or h==i:
                continue
#          print(str(i)+str(j)+str(h))
            print("{0}{1}{2}".format(i,j,h))
            count=count+1
print(count)







