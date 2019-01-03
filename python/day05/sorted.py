# coding:utf-8
class Sorted:
    #   选择排序
    def selection(self, data):
        for i in range(len(data) - 1):
            for j in range(i + 1, len(data)):
                if data[i] > data[j]:
                    data[i], data[j] = data[j], data[i]
            print(data)
        return data

    #   插入排序
    def insertion(self, data):
        d = list(data)
        for i in range(len(d) - 1):
            for j in range(i + 1, len(d)):
                if d[i] > d[j]:
                    k = d[j]
                    d.pop(j)
                    d.insert(i, k)
            print(d)


if __name__ == '__main__':
    data = [9, 1, 4, 7, 6, 8, 5, 2, 3]
    sort = Sorted()
    sort.insertion(data)
