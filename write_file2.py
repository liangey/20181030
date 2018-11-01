#Author:ley
# --*-- coding: utf-8 --*--
#@Time : 2018-10-31 14:37
#@Author: ley
#@Site : 
#@File : write_file2.py
#@Software : PyCharm

f=open('H:\poet.txt','a+')
print(f.read())
fruits= ['appple\n','banana\n','orange\n','watermelon\n']
f.writelines(fruits)
print("写入成功")
f.close()

