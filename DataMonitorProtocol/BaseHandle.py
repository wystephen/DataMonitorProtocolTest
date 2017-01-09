# -*- coding:utf-8 -*-
# carete by steve at  2017 / 01 / 08　22:10
import socket

import time

class BaseHandle:
    '''
    initial the handle.
    '''

    def __init__(self):
        self.just_for_test_connect()



        # Search Masters


        # Connect to Masters

        # Creat Data Send thread(not individual thread)


    def search_master(self,possible_device):

        return 0


    def just_for_test_connect(self):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(('127.0.0.1',1994))

        index = 0
        while True:
            s.send(b'is ok')
            index += 1
            time.sleep(1)
            if(index > 20):
                break
        s.send(b'exit')
        s.close()



if __name__ == '__main__':
    tmp = BaseHandle()


