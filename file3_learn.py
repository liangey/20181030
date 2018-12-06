#Author:ley
# --*-- coding: utf-8 --*--
#@Time : 2018-12-06 9:38
#@Author: ley
#@Site : 
#@File : file3_learn.py
#@Software : PyCharm


f1=open('D:\\sea\\PycharmProjects\\20181030\\test.txt','r+')
f1.write('qd')
f1.close()

#print(f1.readlines())
f2=open('D:\\sea\\PycharmProjects\\20181030\\test.txt','r')
print(f2.readlines())
f2.close()

f3=open('D:\\sea\\PycharmProjects\\20181030\\test.txt','w+')
for line in (i**2 for i in range(1,11)):
    f3.write(str(line)+'\n')
f3.flush()
f3.close()
print(f3)


