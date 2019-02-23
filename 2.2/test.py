import os
import threading
os.chdir('d:/python/')

input_list = []
a=input('请输入目录数量')
a=int(a)

for i in range(a):
    b=input('请输入目录名字')
    input_list.append(b)

def MeiJu(path):
    lock.acquire()
    try:
        files = os.listdir(path)
        for name in files:
            print(name)
    except FileNotFoundError as f:
        print('目录不存在')
    lock.release()

lock = threading.Lock()

def main():
    for i in range(a):
        t = threading.Thread(target=MeiJu,args=(input_list[i],))
        t.start()
        t.join()

if __name__ == "__main__":
    main()