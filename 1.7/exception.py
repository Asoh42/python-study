'''while True:
    try:
        n=input('请输入一个整数')
        n=int(n)
        break
    except ValueError as e:
        print('无效数字,再次输入....',e)
print('输入成功')    
'''

class ShortInputException(Exception):
    def __init__(self,length,atleast):
        Exception.__init__(self)
        self.length=length
        self.atleast=atleast

try:
    s=input('Enter something')
    if len(s)<3:
        raise ShortInputException(len(s),3)
except EOFError:
    print('\n why did you do  an EOF on me?')
except ShortInputException as e:
    print('ShortInputException:The input was of the length%d,\
            was excepting  at least %d '%(e.length,e.atleast))
else:
    print('No exception  was raised')

def test1():
   try:
      print('to do stuff')
      raise Exception('hehe')
   except Exception:
      print('process except')
      print('to return in except')
      return 'except'
   finally:
      print('to return in finally')
      return 'finally'
 
test1Return = test1()
print('test1Return : ' + test1Return)