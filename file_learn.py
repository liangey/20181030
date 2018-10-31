#Author:ley
# --*-- coding: utf-8 --*--
#@Time : 2018-10-31 10:56
#@Author: ley
#@Site : 
#@File : file_learn.py
#@Software : PyCharm
f=open("H:\主脚本.txt")
while True:
    text=f.readline()
    if text:
        print(text)
    else:
        print(len(text))
        break
f.close()