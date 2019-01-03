# coding:utf-8
 # 函数中套函数，递包写法
def add(a,b):
    def test(x):
        if not isinstance(x, float):
            return int(x)
        else:
            return x
    return test(a)+test(b)

print(add(1,'5'))

#  修饰器 ,通过递包写法实现修饰函数，并修饰主函数
def test(func):
    def param(a,b):
        _a = float(a) if not isinstance(a,float) else a
        _b = float(b) if not isinstance(b,float) else b
        return func(_a, _b)
    return param

@test
def sub(a,b):
    return a-b

print(sub(3,'6'))