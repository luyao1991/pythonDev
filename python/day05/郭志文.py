# coding:utf-8
import random


class EightQueens:

    # 冲突检查:用一个元组state记录皇后的位置，每个皇后的位置都可以由其索引和值来表示，
    #  例如，state[0]=2,表示第一行的第三列，next_x代表下一个皇后的列，next_y代表下一个皇后的行
    @staticmethod
    def conflict(state, next_x):
        next_y = len(state)
        for i in range(next_y):
            # 如果下一个皇后的位置与当前的皇后位置相邻（包括上下，左右）或在同一对角线上，则说明有冲突，需要重新摆放
            if abs(state[i] - next_x) in (0, next_y - i):
                return True
        return False

    # 采用生成器的方式来产生每一个皇后的位置，并用递归来实现下一个皇后的位置。
    def queens(self, num, state=()):
        for pos in range(num):
            if not self.conflict(state, pos):
                # 判断是否为最后一个皇后，并返回该皇后的位置信息
                if len(state) == num - 1:
                    yield (pos,)
                # 否则，把当前皇后的位置信息，添加到state里，并传递给下一皇后。
                else:
                    for result in self.queens(num, state + (pos,)):
                        yield (pos,) + result

    # 为了直观表现棋盘，用X表示每个皇后的位置
    @staticmethod
    def pretty_print(solution):
        def line(pos, length=len(solution)):
            return '*   ' * pos + 'X   ' + '*   ' * (length - pos - 1)

        for pos in solution:
            print(line(pos))


if __name__ == "__main__":
    eq = EightQueens()
    print(eq.conflict((),0))
    print(list(eq.queens(4)))
    # eq.pretty_print(random.choice(list(eq.queens(8))))
