class huiwen(Exception):
    def __init__(self):
        Exception.__init__(self)
        

while True:
    try:
        a=input('请输入回文')
        for n in a[:]:
            if n == a[-1]:
                print('yes')
                break
            else:
                raise huiwen()

    except huiwen as e:
        print('回文错误,请继续输入',e)