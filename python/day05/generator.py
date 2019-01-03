# coding:utf-8


#  生成器
class Generator(object):
    def __init__(self, count, price):
        self.count = count
        self.price = price

    def test(self):
        for i in range(self.count):
            yield (i + 1) * self.price


if __name__ == '__main__':
    cart = Generator(5, 0.8)
    print(type(cart))
    good = cart.test()
    print(type(good))
    # print(dir(good))
    # print(good.__next__())
    # print(good.__next__())
    # print(good.__next__())
    # for g in good:
    #     print(g)

# a = (i for i in range(10))
# for i in a:
#     print(i)
