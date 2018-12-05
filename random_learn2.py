#Author:ley
# --*-- coding: utf-8 --*--
#@Time : 2018-11-02 16:36
#@Author: ley
#@Site : 
#@File : random_learn2.py
#@Software : PyCharm

import random
checkcode=''
for i in range(4):
    current=random.randrange(0,4)
    if current != i:
        temp=chr(random.randint(65,90))
    else:
        temp=random.randint(0,9)
    checkcode+=str(temp)
print(checkcode)