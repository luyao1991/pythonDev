# coding=utf-8
from stack import Stack


class Queue(object):

    def __init__(self, size):
        self.size = size
        self.stack1 = Stack(size)
        self.stack2 = Stack(size)

    def push(self, element):
        print('########入队列#########')

        # self.stack1.push(element)
        # print('栈1中的数据为{0}'.format(self.stack1.data))
        # # 如果栈1中数据已满，且栈2中为空，将所有栈1中的数据传入栈2中
        # if self.stack2.empty() and self.stack1.full():
        #     for i in range(self.size):
        #         self.stack2.push(self.stack1.pop())
        # print('栈2中的数据为{0}'.format(self.stack2.data))

        if self.full():
            print('队列已满')
        else:
            return self.stack1.push(element)

    def pop(self):
        print('#########出队列##########')
        print(self.stack1.data)
        print(self.stack2.data)
        #  如果栈2中为空时，先将栈1中的所有数据传入栈2进行出栈，否则直接在栈2中进行出栈
        if not self.stack2.empty():
            return self.stack2.pop()
        else:
            if self.stack1.empty():
                print("队列为空！")
            else:
                while not self.stack1.empty():
                    self.stack2.push(self.stack1.pop())
                return self.stack2.pop()

    def empty(self):
        return self.stack1.empty() and self.stack2.empty()

    def full(self):
        length = self.stack1.length() + self.stack2.length()
        if length == self.size:
            return True
        else:
            return False

    def peak(self):
        print('#########返回元素##########')
        if not self.stack2.empty():
            return self.stack2.peak()
        else:
            if self.stack1.empty():
                print("队列为空！")
            else:
                while not self.stack1.empty():
                    self.stack2.push(self.stack1.pop())
                return self.stack2.peak()

    #  查找栈1、栈2中element对应的index，element可能存在重复值
    def find(self, element):
        if self.stack2.empty():
            return self.stack1.find(element)
        else:
            sf = self.stack1.find(element)
            for i, v in enumerate(sf):
                sf[i] = v + len(self.stack2.data)
            return self.stack2.find(element) + sf


if __name__ == '__main__':
    s = Queue(3)
    print('是否为空:  ', s.empty())
    s.push(1)
    print('是否为空:  ', s.empty())
    s.push('a')
    print(s.pop())
    s.push([1, 2])
    s.push('c')
    print('是否已满:  ', s.full())
    s.push(4)
    s.push('b')
    print(s.pop())
    s.push('b')
    s.push('c')
    print(s.stack1.data)
    print(s.stack2.data)
    print(s.peak())
    print(s.stack1.data)
    print(s.stack2.data)
    print(s.find('b'))
