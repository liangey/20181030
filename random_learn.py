#Author:ley
# --*-- coding: utf-8 --*--
#@Time : 2018-10-31 15:03
#@Author: ley
#@Site : 
#@File : random_learn.py
#@Software : PyCharm

import random
print("生成第1个随机数",random.random())
print("生成第2个随机数",random.random())
#生成第3个随机数,并且大于11小于20
#andom.randint()的函数原型为：random.randint(a, b)，用于生成一个指定范围内的整数
print("生成第3个随机数",random.randint(11,20))

#random.randrange的函数原型为：random.randrange([start], stop[, step])，从指定范围内，按指定基数递增的集合中 获取一个随机数
print("生成第4个随机数",random.randrange(10,18,2))

#random.choice从序列中获取一个随机元素
print("生成第5个随机数",random.choice(["python","java","c#"]))

#random.shuffle的函数原型为：random.shuffle(x[, random])，用于将一个列表中的元素打乱
list=[1,2,3,4,5]
random.shuffle(list)
print(list)

#random.sample的函数原型为：random.sample(sequence, k)，从指定序列中随机获取指定长度的片断。sample函数不会修改原有序列
list2=[1,2,3,4,5,6,7,8]
slice=random.sample(list2,2)
print(slice)
print(list2)


