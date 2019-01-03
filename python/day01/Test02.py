# coding:utf-8
#常用数据类型包括 int,float,str,bool,list,tuple,dict,set等
# nu=float(input("请输入数字："))
# if nu>0:
#     print("整数")
# elif nu<0:
#     print("负数")
# else:
#     print(0)
#
# nu=(0,1,23,4)
# print(type(nu))

#学习成绩>=90分的同学用A表示，60-90分之间的用B表示，60分以下的用C表示
# score=float(input("请输入分数："))
# if score>=90:
#     print("A")
# elif score<60:
#     print("C")
# else:
#     print("B")

#计算个人所得税缴纳额
#	应纳个人所得税税额 = （应纳税所得额 – 3500）× 适用税率- 速算扣除数

money_tax = float(input("应纳税工资所得额："))-3500
if money_tax <= 1500:
    tax = money_tax*0.03
    print("个人所得税为"+str(tax)+"元")
elif 4500 < money_tax <= 9000:
    tax = money_tax * 0.2-555
    print("个人所得税为" + str(tax) + "元")
elif 9000 < money_tax <= 35000:
    tax = money_tax * 0.25-1005
    print("个人所得税为" + str(tax) + "元")
elif 35000 < money_tax <= 55000:
    tax = money_tax * 0.3-2755
    print("个人所得税为" + str(tax) + "元")
elif 55000 < money_tax <= 80000:
    tax = money_tax * 0.35-5505
    print("个人所得税为" + str(tax) + "元")
else:
    tax = money_tax * 0.45 - 13505
    print("个人所得税为" + str(tax) + "元")