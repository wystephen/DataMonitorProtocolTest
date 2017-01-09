# -*- coding:utf-8 -*-
# carete by steve at  2017 / 01 / 09　11:25

import socket

import threading

class TestSimpleHost:
    def __init__(self):
        self.s_handle = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        self.s_handle.bind(('127.0.0.1',1994))

    def 
