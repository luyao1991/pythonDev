# coding:utf-8

# a=16400-5000-3555-1500
# print(a)

def fn(n):
    # a=16400*n - 5000*n - 3555*n - 1500*n
    b = 0
    sum = 0
    for i in range(1, n + 1):
        a = (16400 - 5000 - 3555 - 1500) * i
        sum += b
        if a <= 36000:
            b = round(a * 0.03 - sum, 2)
            print('{0}月份预扣应纳税额为{1}元， 预扣税额是{2}元， 累计扣税为{3}'.format(i, a, b,sum+b))
        elif a > 36000 and a <= 144000:
            b = round(a * 0.1 - sum - 2520, 2)
            print('{0}月份预扣应纳税额为{1}元， 预扣税额是{2}元， 累计扣税为{3}'.format(i, a, b, sum+b))
        else:
            b = round(a * 0.2 - sum - 16920, 2)
            print('{0}月份预扣应纳税额为{1}元， 预扣税额是{2}元， 累计扣税为{3}'.format(i, a, b, sum+b))

    print('月均纳税额为{0}元'.format(round((sum + b) / 12, 2)))


fn(12)
