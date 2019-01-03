#coding=utf-8

import random

money = random.randint(0, 999)

def generate_code(money):
    return list(set([
        money[0] + money[1] + money[2], money[0]+money[2]+money[1],
        money[1] + money[0] + money[2], money[1] + money[2] + money[0],
        money[2] + money[0] + money[1], money[2] + money[1] + money[0],
    ]))

while True:
    code = int(input("请选投注的号码[0~999]："))
    if code >= 0 or code <= 999:
        break

money = "{0:03}".format(money)
code = "{0:03}".format(code)

while True:
    play = int(input("请选择玩法（0-直选 1-组选3 2-组选6）："))
    if play in [0, 1, 2]:
        if play == 0:
            break
        elif play == 1 and len(generate_code(code)) == 3:
            break
        elif play == 2 and len(generate_code(code)) == 6:
            break
        else:
            continue

print("玩法是{0}, 开奖号码是{1}, 选择的号码是{2}".format(play, money, code))
if play == 0:
    if money == code:
        print("恭喜您中奖1000元！")
    else:
        print("多买几张吧，提高中奖概率！")
elif play == 1:
    zuxuan3 = generate_code(money)
    if len(zuxuan3) != 3:
        print("多买几张吧，提高中奖概率！")
    else:
        if code in zuxuan3:
            print("恭喜您中奖320元！")
        else:
            print("多买几张吧，提高中奖概率！")
elif play == 2:
    zuxuan6 = generate_code(money)
    if len(zuxuan6) != 6:
        print("多买几张吧，提高中奖概率！")
    else:
        if code in zuxuan6:
            print("恭喜您中奖160元！")
        else:
            print("多买几张吧，提高中奖概率！")
else:
    print("玩法异常！")