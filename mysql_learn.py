#Author:ley
# --*-- coding: utf-8 --*--
#@Time : 2018-11-01 11:07
#@Author: ley
#@Site : 
#@File : mysql_learn.py
#@Software : PyCharm

import pymysql
#创建连接对象
conn=pymysql.connect(host='',port=3306,user='root',passwd='',db='')
#创建游标
cursor=conn.cursor()
#执行update_sql
effect_now=cursor.execute("update hosts set hosts='1.1.1.1'")
effect_now=cursor.executemany("insert into hosts(host,color_id)values(%s,%s)",[("1.0.0.1",1,),("10.0.0.3",2)])

new_id=cursor.lastrowid
cursor.execute("select * from hosts")
row1=cursor.fetchone()
row2=cursor.executemany(3)
row3=cursor.fetchall()


cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
conn.commit()
cursor.close()
conn.close()

