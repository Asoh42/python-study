from socket import *

HOST = 'localhost'
PORT = 22222
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpclientsock=socket(AF_INET,SOCK_DGRAM)

while True:
    data = raw_input('>')
    if not data:
        break
    udpclientsock.sendto(data ,ADDR)
    data, ADDR = udpclientsock.recvfrom(BUFSIZ)
    if not data:
        break
    print data

udpclientsock.close()