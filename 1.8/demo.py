class Animal:
    def __init__(self,kinds,color):
        self.kinds=kinds
        self.color=color
        print('(Animal is %s,color is %s)'%(self.kinds,self.color))
    def run(self):
        print('%s is running'%(self.kinds))
    def meal(self):
        print('%s is having a meal'%self.kinds)

class Tigers(Animal):
    def __init__(self,kinds,color,size):
        Animal.__init__(self,kinds,color)
        self.size=size
        print('(Kind is %s)'%self.kinds)
    def run(self):
        Animal.run(self)
    def _size(self):
        print('%s\'s size is %s'%(self.kinds,self.size))

class Cock(Animal):
    def __init__(self,kinds,color,size):
        Animal.__init__(self,kinds,color)
        self.size=size
        print('(Kind is %s)'%self.kinds)
    def run(self):
        Animal.run(self)
    def _size(self):
        print('%s\'s size is %s'%(self.kinds,self.size))
t=Tigers('tiger','yello','big')
c=Cock('cock','red','small')
m=[t,c]
for r in m:
    r.run()
    r._size()

