# -*-coding:utf-8 -*-
'''
class Person:
    pass
P = Person()
'''
#创建对象
class Person1:
    def sayhi(self):
        print('hello world')

p = Person1()
p.sayhi()

#构造函数
class Person2():
    def __init__(self,name):
        self.name=name
    def sayhello(self):
        print('hello my name is',self.name)

p2=Person2('zzk')
p2.sayhello()

#变量
class Person3:
    population = 0

    def __init__(self,name):
        self.name=name
        print('(initializes %s)'% self.name)
        Person3.population +=1

    def sayhello(self):
        print('hi,my name is %s'%self.name)

    def howmany(self):
        if Person3.population ==1:
            print('I am the only person here')
        else:
            print('we have %s persons here'%(Person3.population))

y = Person3('aa')
y.sayhello()
y.howmany()

kl = Person3('�考拉')
kl.sayhello()
kl.howmany()
 
y.sayhello()
y.howmany()

#继承 
class SchoolMember:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print('(initialized SchoolMember:%s)'%self.name)
    def tell(self):
        print('name:%s age:%s'%(self.name,self.age))

class Teacher(SchoolMember):
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary=salary
        print('(initialized Teacher:%s)'%self.name)
    def tell(self):
        SchoolMember.tell(self)
        print('Salary:%d'%self.salary)


class Student(SchoolMember):
    def __init__(self,name,age,mark):
        SchoolMember.__init__(self,name,age)
        self.mark=mark
        print('initialized Student:%s'%self.name)
    def tell(self):
        SchoolMember.tell(self)
        print('Mark:%d'%self.mark)

t=Teacher('zzy',20,2300)
s=Student('yyy',18,80)

print()

members=[t,s]
for member in members:
    member.tell()