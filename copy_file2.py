#Author:ley
# --*-- coding: utf-8 --*--
#@Time : 2018-10-31 14:50
#@Author: ley
#@Site : 
#@File : copy_file2.py
#@Software : PyCharm

with open("H:\poet.txt") as src,open("H:\pope3.txt",'w') as dest:
    dest.write(src.read())

print("复制成功")