# coding:utf-8
def sort(data):
    l = len(data)
    for d in range(l):
        for q in range(l-1):
            if data[q] > data[q+1]:
                data[q], data[q+1] = data[q+1], data[q]
    return data


if __name__ == '__main__':
    data = [3, 1, 7, 6, 2, 9, 4, 5, 8]
    sort(data)
    print(data)
    string = ['s','f','a','d','c','b','e']
    sort(string)
    print(string)

# 斐波那契数列


# def f(n):
    # if n==1 or n==0:
    #     return n
    # x,y=0,1
    # for i in range(2,n+1):
    #     x, y = y, x+y
    # return y
    # elif n>1:
    #     return f(n-1)+f(n-2)
#     data = [0, 1]
#     for i in range(2, n + 1):
#         data.append(data[i-1]+data[i-2])
#     return data[n]
#
#
# print(f(1))

# 阶乘
def f(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*f(n-1)


print(f(3))

# 水仙花数
for i in range(10):
    for j in range(10):
        for k in range(10):
            s=str(i)+str(j)+str(k)
            if s not in range(100,1000):
                continue
            if i**3+j**3+k**3==int(s):
                print(s)

# s个n相加
def f(n,s):
    sum=0
    for i in range(1,s+1):
        t=str(n)*i
        sum+=int(t)
    return sum
print(f(2, 1))

# print(sum(list(map(data))))

# 猴子第一天摘了若干桃子，每天都吃了前一天所剩桃子的一半零一个，迟到第10天时桃子只剩下1个，求一共摘了多少个桃子

a=1
for i in range(1, 10):
    a = (a+1)*2
    print(a)


