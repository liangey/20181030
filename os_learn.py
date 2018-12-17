#Author:ley
# --*-- coding: utf-8 --*--
#@Time : 2018-12-14 10:10
#@Author: ley
#@Site : 
#@File : os_learn.py
#@Software : PyCharm

import os
os.getcwd() #获取当前目录
os.chdir()  #改变当前目录
os.curdir #返回当前目录
os.pardir #获取当前目录的父目录字符串名
os.makedirs('dirname1/dirname2') #递归生成多层目录
os.removedirs('dirname1') #若目录为空，则删除。
os.mkdir('dirname1') #生成单机目录
os.rmdir('dirname1') #删除单机空目录，不为空则无法删除
os.listdir('driname1') #列出指定目录下的所有文件和子目录，包括隐藏文件
os.remove() #删除一个文件
os.stat('path/filename') #获取文件，目录信息
os.rename("oldname","newname") #重命名
os.name #输出字符串指示出当前使用平台
os.system("bash command") #运行shell 命令
os.popen()
