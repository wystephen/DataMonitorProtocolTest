# -*- coding:utf-8 -*-
# carete by steve at  2017 / 01 / 25　17:19

import time
import socket

if __name__ == '__main__':
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = ('127.0.0.1',9999)
    sk.connect(address)

    for i in range(100000):
        tmp_info = ('<Name:fast> {0} {1} {2}'.format(i,i*10.0,i*i))

        sk.send(tmp_info.encode('utf-8'))
        time.sleep(0.5)
