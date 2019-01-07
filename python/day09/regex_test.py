# coding:utf-8
import re

a = "eferveVErv3134ef423"
pattern = re.compile(r'\d+')
m=pattern.finditer(a)
print(type(m))
for i in m:
    print(i)

# re.compile(pattern)
