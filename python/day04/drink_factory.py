# coding:utf-8

class Drink(object):

    def __init__(self):
        print("这是饮料")


class Water(Drink):

    def __init__(self):
        print("我是白开水")


class Cola(Drink):

    def __init__(self):
        print("我是可乐")


class Sprint(Drink):

    def __init__(self):
        print("我是雪碧")


class Coffee(Drink):

    def __init__(self):
        print("我是咖啡")


class DrinkFactory(object):

    def __init__(self):
        print("我是饮料工厂")

    def do(self, name):
        if name == '可乐':
            return Cola()
        elif name == '雪碧':
            return Sprint()
        elif name == '咖啡':
            return Coffee()
        else:
            return Water()

# factory = DrinkFactory()
# factory.do(name='健力宝')
# factory.do(name='可乐')
# factory.do(name='咖啡')
# factory.do(name='雪碧')

factory = {
    '可乐': Cola(),
    '雪碧': Sprint(),
    '咖啡': Coffee(),
}
print("这里是华丽的分隔符")
# print(factory)
print(factory.get('可乐', Water()))
print(factory.get('健力宝', Water()))
# for key in factory.keys():
#     print(key)
#     print(factory[key])