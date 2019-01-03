# coding:utf-8
# a='ade dede'

# print(a.capitalize())
# print(a.upper())
# print(a.lower())
# print(a.index("ded"))
# print(a.replace("dedede","bcd"))
# print(a.split(" "))
#
# b="abd\n"       去掉旁边的空白字符如空格和回车
# print(b.strip())
#
# c=["a","b","c"]
# print("-".join(a))

a="external_libraies_cecec_cecrecerv"
b=a.split("_")
for i in range(len(b)):
    b[i]=b[i].capitalize()
print("".join(b))