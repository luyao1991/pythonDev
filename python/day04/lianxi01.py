# coding:utf-8

class Friut():
    price = 0

    # def __init__(self, color, name, taste):
    #     self.color = color
    #     self.name = name
    #     self.taste = taste

    def getprice(self):
        print(Friut.price)

    def getname(self, name):
        print(name)

    def gettaste(self, taste):
        print(taste)


class Apple(Friut):
    price = 8
    def getname(self,name):
        print('这是一个{0}'.format(name))


#
# class Pear(Friut):
#     def getPrice(self):
#         print('这个梨是免费的')
#
# class Banana(Friut):
#     pass
#
# class Watermelon(Friut):
#     pass


if __name__ == '__main__':
    apple = Apple()
    print(apple.price)
    apple.getprice()
    apple.getname('Apple')