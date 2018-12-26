# -*- coding:utf-8
#整型
a = 0o123
print ("a="+str(a))

b = 64
print ('b='+str(b))
c = -123
print ('c='+str(c))

d = 0x80
print ('d='+str(d))
#长整型
longint = 12039480193284091234
print ("logint="+str(longint))
#bool函数
print(bool(1))
print(bool(0))
print(bool(True))
print(bool([]))

from decimal import *
 
print("十进制浮点....")
dec=Decimal('.1')
print(dec)
print(Decimal(.1))
print(dec +Decimal(.1))

#转换工厂
print(int(2.33))
print(float(4))
print(complex(2))#虚数

#进制转换
print(hex(0o1234))
print(oct(0x1234ff))

#ascii转换
print(chr(97))
print(ord("a"))