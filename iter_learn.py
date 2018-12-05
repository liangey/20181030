#Author:ley
# --*-- coding: utf-8 --*--
#@Time : 2018-12-05 14:12
#@Author: ley
#@Site : 
#@File : iter_learn.py
#@Software : PyCharm
import  os
L=[1,2,3,4,5]
L=[x+20 for x in L]

print(L)

L2=[x**2 for x in range(10) if x % 2==0]
print(L2)


res=[x+y for x in [0,1,2] for y in [100,200,300]]
print(res)

x1=[x for x in range(10)]
print(x1)

x2=[x**2 for x in range(10)]
print(x2)

x3=[x**2 for x in range(10) if x ** 2 <50 ]
print(x3)

x4=[(x+1,y+1) for x in range(2) for y in range(2)]
print(x4)

N=(i**2 for i in range(1,11))
print(N)
#此处返回的是一个生成器的地址
print(N.__next__())
print(N.__next__())
print(N.__next__())

F=(file for file in os.listdir('/var/log') if file.endswith('.log'))
print(F)