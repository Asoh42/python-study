# -*- coding:UTF-8 -*-
#if判断语句
x=int(input('请输入一个整数'))
if x==0:
    print('%d==0' %x)
elif x<0:
    print('%d<0' %x)
else:
    print('%d>0' %x)
#for迭代
print('for 测试....')
words=['cat','window','defenestrate']
for word in words:
    print(word,len(word))
#for根据序列用切片进行迭代
for word1 in words[:]:
    if len(word1)>6:
        words.insert(0,word1)
print(words)
#while循环
a=0
while(a<9):
    print('a=%d'%a)
    a+=1
#进行等差计算
x=range(10)
y=range(1,10)
z=range(1,10,3)
print(x)
print(y)
for i in z:
    print('value is ',i)
#break 跳出循环
print('break....')
for ab in range(2,10):
    for c in range(2,ab):
        if ab % c==0:
            print(ab,' euqal ',c,'*',ab//c)
            break
    else:
        print(ab,' is prime number')

#continue 继续循环
print('continue....')
for d in range(1,10):
    if d % 2==0:
        continue
    print(d)
    