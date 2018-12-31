def logo(Username,Password):
    '''简单的登陆
        帐号
        密码'''
    username = input('请输入帐号:')
    password = input('请输入密码:')
    if username == 'seven' and password == '123':
        print('login success')
    else:
        print('login failed')
a='username'
b='password'
logo(a,b)
print(logo.__doc__)


def whilexunhuan(num1,num2):
    '''2-3+4-5+.....+100'''
    result=0
    num1=int(num1)
    num2=int(num2)
    while num1<=num2:
        if num1%2==0:
            result+=num1
        else:
            result-=num1
        num1+=1
    print(result)
print(whilexunhuan.__doc__)
whilexunhuan(2,100)