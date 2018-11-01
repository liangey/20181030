#Author:ley
# --*-- coding: utf-8 --*--
#@Time : 2018-11-01 10:53
#@Author: ley
#@Site : 
#@File : write_file3.py
#@Software : PyCharm

with open('pope.txt','r') as f1,open('dist_new.txt','w') as f2:
    i=0
    for line in f1:
        i+=1
        if i%100==0:
            f2.write(line)
