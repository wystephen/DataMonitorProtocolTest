# -*- coding:utf-8 -*-
# carete by steve at  2017 / 01 / 09　11:25

import socket

import threading

class TestSimpleHost:
    def __init__(self):
        self.s_handle = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        self.s_handle.bind(('127.0.0.1',1994))
        self.s_handle.listen(10)

        while True:
            sock, addr = self.s_handle.accept()

            t = threading.Thread(target=self.VirtualBuildConnect,args=(sock,addr))
            t.start()


    def VirtualBuildConnect(self,sock,addr):
        print("Accept new connect from {0}".format(addr))

        sock.send(b'Welcom')

        while True:
            data = sock.recv(1024)

            if data == 'close' :
                break
            else:
                print("data is : ")

        sock.close()
        print("Connection from {1} closed.".format(addr))

if __name__ == '__main__':
    tmp = TestSimpleHost()