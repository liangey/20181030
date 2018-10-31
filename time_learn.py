#Author:ley
# --*-- coding: utf-8 --*--
#@Time : 2018-10-31 17:00
#@Author: ley
#@Site : 
#@File : time_learn.py
#@Software : PyCharm

import  time
import datetime
t="2017-11-24 17:30:00"
#将其转换为时间数组
timeStuct=time.strptime(t,"%Y-%m-%d %H:%M:%S")
print(timeStuct)
#转换为时间戳:
timeStmp=int(time.mktime(timeStuct))
print(timeStmp)

#时间戳转换为指定格式日期
localTime=time.localtime(timeStmp)
strTime=time.strftime("%Y-%m-%d %H:%M:%S",localTime)
print(strTime)

#获取当前时间并转换为指定日期格式
now=time.time()
print(now)
localTime2=time.localtime(now)
strTime2=time.strftime("%Y-%m-%d %H:%M:%S",localTime2)
print(strTime2)

#获得三天前的时间的方法
threeDays=(datetime.datetime.now() - datetime.timedelta(days=7))

timeStmp2=int(time.mktime(threeDays.timetuple()))
print(timeStmp2)
strTime3=threeDays.strftime("%Y-%m-%d %H:%M:%S")
print(strTime3)