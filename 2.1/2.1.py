#-*-coding:utf-8 -*-
import os
import sys

#文件读取
file = open('./1.txt','r')
print(file.read())
file.close()

#读取部分内容
print('读取部分内容....')

file=open('./1.txt','r')
print(file.read(3))

print('二进制模式....')

file=open('./1.txt','rb')
print(file.read())
file.close()

#逐行读取
'''print('逐行读取....')
file=open('./1.txt','r')
for c in file:
    print(c)
file.close()
'''
#分批读取
'''print('分批读取.....')
with open ('./1.txt','r') as f:
    while True:
        c = f.read(1)
        if not c:
            break
        print(c)
'''
#文件写入
filePath='./1.txt'

print('a模式写入....')

def printContent(path):
    with open(path,'r') as f:
        print(f.read())

with open(filePath,'a') as f: #a是在后面追加内容
    f.write('\n追加内容\r\n')

printContent(filePath)

#文件的创建、删除、重命名
def removeTest():#os.remove(path) path是路径
    os.remove('./1.txt')

def renameTxt():#os.rename(src,dst)
    os.rename('./1.txt','/abc.txt')