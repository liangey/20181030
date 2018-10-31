#Author:ley
# --*-- coding: utf-8 --*--
#@Time : 2018-10-31 15:47
#@Author: ley
#@Site : 
#@File : orglist_learn.py
#@Software : PyCharm

orgList=[1,0,3,7,7,5]
#list()方法是把字符串str或元组转成数组
#set和其他语言类似, 是一个无序不重复元素集
formatlist=list(set(orgList))
print(formatlist)

#使用keys()方法
orgList2=[1,0,3,8,8,5,5]
formatlist2=list({}.fromkeys(orgList2).keys())
print(formatlist2)

#循环遍历法
orgList3=[1,0,3,8,8,5,5]
formatlist3=[]
for i in orgList3:
    if i not in formatlist3:
        formatlist3.append(i)

print(formatlist3)

#按照索引再次排序
orgList4=[1,0,3,8,8,5,5]
formatlist4=list(set(orgList4))
formatlist4.sort(key=orgList4.index)
print(formatlist4)