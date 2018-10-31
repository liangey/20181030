#Author:ley
# --*-- coding: utf-8 --*--
#@Time : 2018-10-31 15:39
#@Author: ley
#@Site : 
#@File : requests_learn.py
#@Software : PyCharm
import requests
result=requests.get('http://www.baidu.com')
print(result.text)