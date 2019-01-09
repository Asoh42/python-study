#-*-coding:utf-8 -*-
import sys
import os

os.chdir('c:/Users/admin/Desktop/py/dir')#将当前的路径进行切换

#目录的枚举
def listCurrentDirectory(path):
    files=os.listdir(path)#枚举当前目录下的文件与子目录
    for name in files:
        print(name)

listCurrentDirectory('.')

#获得目录更详细的信息 用os.stat
def listDirectoryDetail(path):
    files = os.listdir(path)
    for name in files:
        pathName = os.path.join(path,name)
        print(os.stat(pathName).st_mode) #inode 保护模式
        print(os.stat(pathName).st_ino) #inode 节点号
        print(os.stat(pathName).st_dev) #inode 驻留的设备
        print(os.stat(pathName).st_nlink) #inode 的链接数
        print(os.stat(pathName).st_uid) #所有者的用户ID
        print(os.stat(pathName).st_gid) #所有者的组ID
        print(os.stat(pathName).st_size) #文件的大小，普通文件以字节为单位的大小；包含等待某些特殊文件的数据
        print(os.stat(pathName).st_atime  )#文件最后访问时间
        print(os.stat(pathName).st_mtime  )#文件最后修改时间
        print(os.stat(pathName).st_ctime  )#由操作系统报告的"ctime"。在某些系统上（如Unix）是最新的元数据更改的时间，在其它系统上（如Windows）是创建时间

listDirectoryDetail('.')   

#解析stat模块的st_mode
import stat

def listCurrentDirectoryMode(path):
    files = os.listdir(path)
    for name in files:
         pathName = os.path.join(path, name)
         mode = os.stat(pathName).st_mode
         
         if stat.S_ISDIR(mode):
            # 如果是目录
            print('%s是文件夹' % pathName)
         elif stat.S_ISREG(mode):
            # 如果是文件
             print('%s是文件'%pathName)
         else:
            # 未知类型
            print('�未知目录类型 %s' % pathName)
         print(stat.filemode(mode))
         
         '''
         if stat.S_ISREG(mode):           #判断是否一般文件
            print('Regular file.')
         elif stat.S_ISLNK (mode):         #判断是否链接文件
            print ('Shortcut.')
         elif stat.S_ISSOCK (mode):        #判断是否套接字文件    
            print ('Socket.')
         elif stat.S_ISFIFO (mode):        #判断是否命名管道
            print ('Named pipe.')
         elif stat.S_ISBLK (mode):         #判断是否块设备
            print ('Block special device.')
         elif stat.S_ISCHR (mode):         #判断是否字符设置
            print ('Character special device.')
         elif stat.S_ISDIR (mode):         #判断是否目录
            print ('directory.')'''

listCurrentDirectoryMode('.')

#目录遍历 os.walk()方法

def walkDir(path):
    for dirName,subdirList,fileList in os.walk(path):
        print('发现目录: %s'%dirName)
        for fname in fileList:
            print('\t%s'%fname)

walkDir('.')

#权限修改 os.chmod(path, mode)
'''
stat.S_IXOTH: 其他用户有执行权0o001
stat.S_IXOTH: 其他用户有执行权0o001
stat.S_IWOTH: 其他用户有写权限0o002
stat.S_IROTH: 其他用户有读权限0o004
stat.S_IRWXO: 其他用户有全部权限(权限掩码)0o007
stat.S_IXGRP: 组用户有执行权限0o010
stat.S_IWGRP: 组用户有写权限0o020
stat.S_IRGRP: 组用户有读权限0o040
stat.S_IRWXG: 组用户有全部权限(权限掩码)0o070
stat.S_IXUSR: 拥有者具有执行权限0o100
stat.S_IWUSR: 拥有者具有写权限0o200
stat.S_IRUSR: 拥有者具有读权限0o400
stat.S_IRWXU: 拥有者有全部权限(权限掩码)0o700
stat.S_ISVTX: 目录里文件目录只有拥有者才可删除更改0o1000
stat.S_ISGID: 执行此文件其进程有效组为文件所在组0o2000
stat.S_ISUID: 执行此文件其进程有效用户为文件所有者0o4000
stat.S_IREAD: windows下设为只读
stat.S_IWRITE: windows下取消只读
'''

#设置文件可以通过用户组执行
'''
os.chmod('./1.txt',stat.S_IXGRP)

#设置文件可以被其他用户写入
os.chmod('./1.txt',stat.S_IWOTH)
'''
#目录的重命名、创建、删除 rename 只能重命名到已存在的路径/  renames 可以移到不存在的路径 可以实现递归重命名
'''
def renameTest():
    walkDir('.')
    os.rename('1.txt','2.txt')
    try:
        os.rename('./a/a.a','./b2/b.b')
    except FileNotFoundError as e:
        print(e)
    os.renames('./a/a.b','./aa/a.a')
    walkDir('.')

renameTest()
'''
#文件目录创建 makedirs(name, mode=0o777, exist_ok=False)

'''def createPath(p):
    try:
        os.makedirs(p)
    except OSError as e:
        print('创建目录失败',e)

    else:
        print('目录%s创建成功'%p)

createPath('./ymz')
'''

def createPath2(p):
    try:
        if not os.path.exists(p):
            os.makedirs(p)
            print('%s创建成功'%p)
        else:
            print('%s已经存在'%p)
    except OSError as e:
        print('创建目录失败',e)

createPath2('./ymz')
createPath2('./bb')

def createPath3(p,mode):
    try:
        if not os.path.exists(p):
            os.makedirs(p,mode)
            print('%s创建成功'%p)
            mode = os.stat(p).st_mode
            print(stat.filemode(mode))
        else:
            print('%s已经存在'%p)

    except OSError as e:
        print('创建目录失败',e)

createPath3('./bbb',0o766)

#创建临时目录 通过tempfile模块可以创建临时目录。

import tempfile
def createTempDirectory():
    with tempfile.TemporaryDirectory() as directory:
        print('临时目录%s'%directory)

createTempDirectory()

#目录删除  
def removeDir(path):
    try:
        os.rmdir(path)
    except OSError:
        print('删除%s失败'%path)
    else:
        print('删除%s成功'%path)

'''
递归删除用os.removedirs方法
'''