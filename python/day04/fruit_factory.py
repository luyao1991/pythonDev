# coding:utf-8

class Friut(object):
    def __init__(self):
        print('这是水果')


class Apple(Friut):
    def __init__(self):
        print('这是苹果')


class Pear(Friut):
    def __init__(self):
        print('这是梨')


class Banana(Friut):
    def __init__(self):
        print('这是香蕉')


class Watermelon(Friut):
    def __init__(self):
        print('这是西瓜')


class FruitFactory():
    def __init__(self):
        print('这是水果')

    def do(self,name):
        if name == '苹果':
            return Apple()
        elif name == '梨':
            return Pear()
        elif name == '香蕉':
            return Banana()
        else:
            return Watermelon()


# if __name__ == '__main__':
factory = {
        '苹果': Apple(),
        '梨': Pear(),
        '香蕉': Banana(),
        '西瓜': Watermelon()
    }
print(factory.get('苹果'))
# factory = FruitFactory()
# factory.do( '苹果')
    # factory.get('香蕉')
