# coding:utf-8
class Queue(object):

    def __init__(self, size):
        self.size = size
        self.data = []

    def push(self, element):
        if self.size > len(self.data):
            self.data.append(element)
        else:
            print('队列已满')

    def pop(self, index=0):
        if not self.data:
            return None
        else:
            try:
                return self.data.pop(index)
            except IndexError:
                return None

    def full(self):
        return len(self.data) == self.size

    def empty(self):
        return not bool(self.data)

    def peak(self, index=0):
        if not self.data:
            return None
        else:
            return self.data[index]

    def find(self, element):
        return self.data.index(element)


if __name__ == '__main__':
    q=Queue(3)
    print(q.empty())
    q.push(1)
    q.push(2)
    q.push(3)
    print(q.data)
    print(q.full())
    q.push(4)
    print(q.pop())
    q.push(4)
    print(q.peak())