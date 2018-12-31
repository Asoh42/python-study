# -*- coding:UTF-8 -*-
import sys
import myModule

print('The command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is ',sys.path,'\n')

#name
if __name__=='__main__':
    print('当前属于单独运行')
else:
    print('当前被导入')

#导入模块
myModule.say()
print('Version is ',myModule.version)