from socket import *

HOST = '192.168.1.7'
PORT = 2133
ADDR = (HOST,PORT)
BUFSIZ = 1024

tcpClient = socket(AF_INET,SOCK_STREAM)
tcpClient.connect(ADDR)


while True:
    data=tcpClient.recv(BUFSIZ)
    if not data:
        break
    tcpClient.send(data)

tcpClient.close()
