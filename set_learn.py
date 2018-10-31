__author__ = 'H005333'
a=set('boy')
a.add('python')
a.update('linux')
a.remove('python')
print(a)


def hello(name):
    return 'hello,' + name + '!'
print(hello('jack'))

names=['ada','amy','tom','tom']
del names[1]
print(names)
#names.append('jack')
names.count('count')
print(names)


try:
    a=10
    b=0
    print(a/b)
except ZeroDivisionError:
    print("除以0错误，捕获异常")


























