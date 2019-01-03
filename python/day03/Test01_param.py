# coding:utf-8
#  a为必备参数；
# 8为默认参数；且默认参数必须在必备参数与可变参数之后
# args为可变参数，通过*声明，且输出类型为tuple
# kargs为关键字参数，通过**声明，切输出为dict
def test(a , *args, b='8',  **kargs,):
    print(a)
    print(b)
#    print([i for i in args])
    print(list(args))
    print(kargs)
test(6,1,2,3,4,5,33,f=2,t=6)