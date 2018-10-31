def printme(str):
    "This is a password string into this function"
    print(str)
    return

print("This is Frist")
print("This is Second")


def changme(mylist):
    "This is a chanmge for me"
    print("values is change",mylist)
    mylist[2]=50
    print("after values is change", mylist)
    return

mylist=[10,20,30]
changme(mylist)

