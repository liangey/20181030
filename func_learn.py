#Author:ley
# --*-- coding: utf-8 --*--
#@Time : 2018-12-17 13:45
#@Author: ley
#@Site : 
#@File : func_learn.py
#@Software : PyCharm

def fun(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

#fun(1,2,3,4,name="leo")

tup=(11,12,13)
dic={"name":"hello","age":20}
fun(1,2,*tup,**dic)

def summ(a,b):
    print("将要计算两个变量相加")
    #return "abc"
    res=a+b
    return res

num1=int(input("请输入一个整数:"))
num2=int(input("请输入另外一个整数:"))

rr=summ(num1,num2)

print(rr)