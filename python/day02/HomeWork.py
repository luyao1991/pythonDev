# coding:utf-8
# 练习一
a='abc'
b='bcd'
c='cfmjfwf!zpvstfmg"'
# 根据例子可知加密规则为每个字符对应的ASCII码值加一,则密文c的明文为ASCII码减一后对应的字符
# 定义一个空字符串
char_c = ''
# 循环取出密文中的每个字符
for i in c:
    # 得到每个字符对应ASCII码值减一的数字，即为明文字符所对应的ASCII码
    j = ord(i)-1
    #得到ASCII对应的字符
    k = chr(j)
    char_c += k
# 输出明文
print(char_c)
#  练习二
#  字符串转整数:输入一组字符串，将字符串中的每个字符取出，在不使用str转int函数的方式下将取出的字符转化为整数，输入的字符串
#  均为正常输入，不包含特殊字符。考虑字符串首位可能有正负号

string = input('请输入字符串')
# print(ord(i) for i in string)
#  i为索引，v为字符值
# s = 0
# for i, v in enumerate(string[::-1]):
#     if v != '-' and v != '+':
#         k = (ord(v)-48)*10**i
#         s += k
s = sum([(ord(v) - 48) * 10 ** i for i,v in enumerate(string[::-1]) if v != '-' and v != '+'])
if string[0] != '-':
    print(s)
else:
    print(s*-1)

#  练习三


