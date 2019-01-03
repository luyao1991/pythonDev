# coding:utf-8
# 输入年月日，判断是一年的第几天？
class HomeWork:

    def which_day (self):
        # 输入年份并判断格式是否正确
        year = int(input("请输入年："))
        while 2018<year or year< 0:
            year = int(input("输入有误请重新输入："))
        # 输入月份并判断格式是否正确
        month = int(input("请输入月："))
        while month not in range(1, 13):
            month = int(input("输入有误请重新输入："))
        # 输入天并判断格式是否正确
        day = int(input("请输入日："))
        while day not in range(1, 32):
            day = int(input("输入有误请重新输入："))
        if year % 4 == 0 or (year % 100 != 0 and year % 400 == 0):
            while month==2 and day not in range(1, 30):
                day = int(input("输入有误请重新输入："))
        else:
            while month==2 and day not in range(1, 29):
                day = int(input("输入有误请重新输入："))
        #闰年每月天数
        month_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        s = 0
        # 当月份为1月时
        if month == 1:
            print("这是今年的第{0}天".format(day))
        # 当年份非闰年时
        else:
            for i in range(month - 1):
                s = s + month_leap[i]
            if year % 4 != 0:
                print("这是{0}年的第{1}天".format (year,s+day-1))
            else:
                print("这是{0}年的第{1}天".format (year,s+day))

if __name__ == '__main__':
    day = HomeWork()
    day.which_day()