# coding:utf-8
import os

file_normal = open('./bbe.txt', 'r+')
# file_transed=open(zfile,'a+')
file_list = file_normal.read().split(' ')
zfile_list = list(set(file_list))
print(zfile_list)
print(len(zfile_list))
