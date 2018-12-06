#Author:ley
# --*-- coding: utf-8 --*--
#@Time : 2018-12-06 14:39
#@Author: ley
#@Site : 
#@File : re_module_learn.py
#@Software : PyCharm

import re
#从开始位置匹配，如果开头没有则无
re.match()
#搜索整个字符串
re.search()
#搜索整个字符串，返回一个list
re.findall()

#r(raw)用在pattern之前，表示单引号中的字符串为原生字符，不会进行任何转义
re.match(r'l','liyuan1').group()   #返回1
re.match(r'y','liyuan') #返回0
re.search(r'y','liyuan1').group() #返回1


#正则表达式可以包含一些可选标志修饰符来控制匹配的模式。
# 修饰符被指定为一个可选的标志。
# 多个标志可以通过按位 OR(|) 它们来指定。如 re.I | re.M 被设置成 I 和 M 标志：

''''
re.I	使匹配对大小写不敏感
re.L	做本地化识别（locale-aware）匹配
re.M	多行匹配，影响 ^ 和 $
re.S	使 . 匹配包括换行在内的所有字符
re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
'''