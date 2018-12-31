# -*- coding:UTF-8 -*-
#函数声明
def sayHello():
    print('hello world')
sayHello()#函数调用

#函数参数
def printMax(a,b):
    if a>b:
        print(a,'is a maxinum')
    else:
        print(b,'is a maxinum')
printMax(5,7)

#docstrings
def printmax(x,y):
    '''hello 

    world.'''
    x=int(x)
    y=int(y)
    
    if x>y:
        print(x,'is a maxinum')
    else:
        print(y,'is a maxinum')
print('---------')
printmax(3,5)
print(printmax.__doc__)
