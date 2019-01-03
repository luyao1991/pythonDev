# coding:utf-8
class Test:
    def __init__(self, a, c):
        self.a = a
        self.c = c

    def get_c(self):
        Test.get_a()
        print(self.c)

    def get_a(self):
        print(self.a)


if __name__ == '__main__':
    test = Test(1, 2)
    test.get_a()
