#Author:ley
# --*-- coding: utf-8 --*--
#@Time : 2018-10-31 14:39
#@Author: ley
#@Site : 
#@File : delete_file.py
#@Software : PyCharm

import os,os.path
if os.path.exists("sd.txt"):
    os.remove("sd.txt")
else:
    print("文件不存在")