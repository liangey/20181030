#Author:ley
# --*-- coding: utf-8 --*--
#@Time : 2018-10-31 14:34
#@Author: ley
#@Site : 
#@File : wirte_file.py
#@Software : PyCharm

#以写的模式打开文件
f=open('H:\poet.txt','w',encoding='utf-8')
f.write('你好,python')
print('写入完毕，运行')
f.close()

