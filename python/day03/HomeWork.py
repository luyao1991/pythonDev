# coding:utf-8
"""
    大厅里有100盏吊灯，每盏灯都编了号码，分别为1-100.每盏灯有一个开关控制。（开关按一下
    灯亮，再按一下灯灭。开关的编号与被控制的等相同。）开始时，灯是全灭的。现在按照以下的
    规则按动开关。现在按照以下规则按动开关。
    第一次，将所有灯点亮。
    第二次将所有的2的倍数的开关按一下。
    第三次，将所有3的倍数的开关按一下。
    以此类推。第N次，将所有N的倍数的开关按一下，问第100次按完之后，大厅里还有几盏灯适亮的？
"""


def lamp(n):
    #  定义100栈灯的编号及对应状态：0为关闭状态，1为打开状态
    lamp_status = {x: 0 for x in range(1, 101)}
    # print(lamp_status)
    lamp_keys = list(lamp_status.keys())
    # print(lamp_keys)
    # 更改灯的状态
    num = 1
    while num <= n:
        # 将所有灯按编号对N取余数，余数为零则为N的倍数，符合更改状态条件
        for i in lamp_keys:
            if i % num == 0:
                if lamp_status[i] == 0:
                    lamp_status[i] = 1
                else:
                    lamp_status[i] = 0
        print('运行{0}次，第{1}次'.format(n, num))
        print(lamp_status)
        num += 1
    #  输出所有亮灯的编号
    # lamp_open = []
    # for i in lamp_keys:
    #     if lamp_status[i] == 1:
    #         lamp_open.append(i)

    print([i for i in lamp_keys if lamp_status[i] == 1])


#  运行100次开关规则
lamp(100)
