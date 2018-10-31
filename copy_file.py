#Author:ley
# --*-- coding: utf-8 --*--
#@Time : 2018-10-31 14:40
#@Author: ley
#@Site : 
#@File : copy_file.py
#@Software : PyCharm

srcFile=open("H:\poet.txt")
destFile=open("H:\poet2.txt",'w')
destFile.write(srcFile.read())
destFile.close()
srcFile.close()
print("复制完成")