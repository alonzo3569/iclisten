# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 12:07:30 2020

@author: logan
"""

import socket
HOST = '192.168.1.109'
PORT = 51678
# Cammand 62726 ; Time Series(TCP)	51678 ; 

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket()
# socket.SOCK_DGRAM: UDP ; socket.SOCK_STREAM: TCP

s.connect((HOST, PORT))
msg=b'\x33\x2a\x00\x04\x00\x00\x00\x00'
s.send(msg)
my_file = open('./test.txt','w')
a=1

while a<10:
    data = s.recv(4096, socket.MSG_WAITALL) #bytes # Keep reading unread part from msg
    my_file.write('Data: \n')
    my_file.write(str(data))
    my_file.write('\n')
    my_file.write('Data length: \n')
    my_file.write(str(len(data)))
    my_file.write('\n')
    print ('Recieved', data)
    #print ('Recieved', type(data))
    a=a+1
    #break

s.close()
my_file.close()
