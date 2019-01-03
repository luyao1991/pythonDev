# coding:utf-8
import math


#   定义函数返回 ax2 + bx + c = 0 的两个解
#   判别式s=b*b-4*a*c
def quadratic(a, b, c):
    s = b * b - 4 * a * c
    if a == 0:
        x = -c / b
        return x
    elif s == 0:
        x = -b / (2 * a)
        return x
    elif s < 0:
        return 'No Answer'
    else:
        x = (math.sqrt(s) - b) / (2 * a)
        y = (-math.sqrt(s) - b) / (2 * a)
        return x, y


print(quadratic(1, 0,-1))
