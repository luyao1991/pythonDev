# coding:utf-8
#  假设有m个小朋友围城一圈，从1开始报数，报n的下朋友出圈，最后剩下
# 的小朋友是几号？
# 解法一
def nm(m,n):
    child = [i for i in range(1,m+1)]
    count=1
    while len(child)>1:
        print('{0}-{1}   {2}'.format(count, n, child))
        c = child.pop(0)
        if count == n:
            count=1
        else:
            count+=1
            child.append(c)
    print(child)
nm(10,2)

#  解法二

def mn(m,n):
    child = [i for i in range(1, m + 1)]
    while len(child)>1:
        index=(n-1)%m
        child=child[index+1:]+child[0:index]
    print(child)
mn(10,2)