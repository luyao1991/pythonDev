# coding=utf-8


# 斐波那契数列
class Fibonacci(object):

    def __init__(self, n):
        self.n = n
        self.index = 0
        self.iterator = [0, 1]
        for i in range(2, self.n + 1):
            self.iterator.append(self.iterator[i - 1] + self.iterator[i - 2])

    # 递归法实现
    def recursion(self, n):
        if n == 0 or n == 1:
            return n
        return self.recursion(n - 1) + self.recursion(n - 2)

    # 递推法实现
    def expression(self, n):
        x, y = 0, 1
        if n == 0 or n == 1:
            return n
        for i in range(2, n + 1):
            x, y = y, x + y
        return y

    #  列表法实现
    def list_or_stack(self, n):
        data = [0, 1]
        for i in range(2, n + 1):
            data.append(data[i - 1] + data[i - 2])
        return data[-1]

    #  迭代器实现
    def __iter__(self):
        return self

    def __next__(self):
        if self.index <= self.n:
            data = self.iterator[self.index]
            self.index += 1
            return data
        else:
            raise StopIteration

    # 生成器实现
    def generator(self):
        for i in self.iterator:
            yield i


if __name__ == '__main__':
    fib = Fibonacci(8)
    print(fib.recursion(8))
    print(fib.expression(8))
    print(fib.list_or_stack(8))
    for f in fib:
        print(f)
    gen = fib.generator()
    for g in gen:
        print(g)
