# coding:utf-8

#  迭代器
class Cup(object):

    def __init__(self):
        self.index = 0
        self.good = [1, 3, 5, 6]

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.good):
            data = self.good[self.index]
            self.index += 1
            return data
        else:
            raise StopIteration

    # def next(self):
    #     return self.__next__()


if __name__ == '__main__':
    cup = Cup()
    for i in cup:
        print(i)