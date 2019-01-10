import optparse
import socket
from scapy.all import *
import time

#FLAG1=F!.F2.F3

def tcpconnscan(host,port):
    try:
        conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        conn.connect((host,port))
        print('[+]%d/tcp open'%port)
    except:
        pass

#FLAG2=F4.F5

def udpconnscan(host,port):
    try:
        rep = sr1(IP(dst=host)/UDP(dport=port), timeout=1,verbose=0)
        time.sleep(1)
        if (rep.haslayer(ICMP)):
            print('[-]%d/udp not open'%port)
    except:
        print('[+]%d/udp open'%port)

#FLAG3=F6.F7.F8

def portscan(host):
    for port in range(1,1023):
        tcpconnscan(host,port)


def main():
    parser = optparse.OptionParser('usage%prog'+'-H <target host>')
    parser.add_option('-H',dest='tgtHost',type='string',help='specify target host')
    (option,args)=parser.parse_args()
    host = options.tgtHost
    if host == None:
        print (parser.usage)
        exit(0)
    portscan(host)

#FLAG7=F9.F10

if __name__ == '__main__':
    main()