import operator

#  返回由商和余数组成的元组
print(divmod(7,3))
#  返回一个数的n次方值
print(pow(5,4))
#   cmp(x,y) 函数用于比较2个对象，如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。
#   Python 3.X 的版本中已经没有 cmp 函数，如果你需要实现比较功能，需要引入 operator 模块，适合任何对象
print(operator.lt(4,3))

print(bin(5))
print(oct(5))
print(hex(5))
print(chr(97))
print(ord('a'))

