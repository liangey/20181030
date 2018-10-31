#Author:ley
# --*-- coding: utf-8 --*--
#@Time : 2018-10-31 14:27
#@Author: ley
#@Site : 
#@File : file_learn2.py
#@Software : PyCharm

f=open("H:\主脚本.txt")
while True:
    line_list=f.readlines()
    print(type(line_list))
    for line in line_list:
        print(line)
    f.close()
