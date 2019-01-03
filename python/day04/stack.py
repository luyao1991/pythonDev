# coding:utf-8
class Stack(object):
    def __init__(self, size):
        self.size = size
        self.data = []

    def push(self, element):
        if self.size > len(self.data):
            self.data.append(element)
        else:
            print('栈已满')

    def pop(self, index=-1):
        try:
            if not self.data:
                return None
            else:
                return self.data.pop(index)
        except IndexError:
            return None

    def full(self):
        return len(self.data) == self.size

    def empty(self):
        return not bool(self.data)

    def peak(self, index=-1):
        try:
            if not self.data:
                return None
            else:
                return self.data[index]
        except IndexError:
            return None

    def find(self, element):
        return [i for i, v in enumerate(self.data) if v == element]

    def length(self):
        return len(self.data)


if __name__ == '__main__':
    s = Stack(3)
    print(s.empty())
    s.push('a')
    s.push('a')
    # s.push(3)
    # s.push(4)
    print(s.data)
    # print(s.full())
    # print(s.pop())
    print('##########')
    s.find('a')
