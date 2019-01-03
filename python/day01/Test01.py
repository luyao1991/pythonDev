# coding:utf-8
# print("    *\n   ***\n  *****\n*******\n  *****\n   ***\n    *")
# print(input("请输入："))

# for i in range(1, 8, 2):
#     for n in range(i):
#         print("*")

# pi=3.14159
# print(type(pi))
# print(int(pi))
# print(str(pi))

# price=input("请输入商品价格：")
# pay=float(price)*0.88
# print("您需要付款："+str(pay)+"元")
# print("您需要付款：{0:015.3f}元".format(pay))
#{0:.5f}     5之后加f为小数点之后保留位数，不加为全部保留位置

file=open("test01.txt", "w+", "encoding=utf-8")
file.write("插入第一行\n插入第二行")
print(file.read())
file.close()

