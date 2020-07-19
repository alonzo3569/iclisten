# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 12:07:30 2020

@author: logan
"""

import socket
from struct import pack, unpack

HOST = '192.168.1.109'
PORT = 51678
# Cammand 62726 ; Time Series(TCP)	51678 ; 

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket()
# socket.SOCK_DGRAM: UDP ; socket.SOCK_STREAM: TCP

s.connect((HOST, PORT))

# Sending Start stream message
msg=b'\x33\x2a\x00\x04\x00\x00\x00\x00'
s.send(msg)
my_file = open('./data5.txt','w')
volt_file = open('./volt_msg5.txt','w')
hexa_file = open('./hexa_msg5.txt','w')
a=1

while a<10000:

    # Every msg will start with header msg and sync
    data = s.recv(2)
    ##
    my_file.write('Data: \n')
    my_file.write(str(data))

    
    # Get message type
    (msg_type, sync) = unpack('!cB',data)
    ##
    my_file.write(f'Msg_type: {msg_type} ; Sync: {sync}\n')

    # Check sync
    if sync != 0x2A:
      break

    # Get payload length
    data = s.recv(2, socket.MSG_WAITALL)
    ##
    my_file.write('Data: \n')
    my_file.write(str(data))
    (payload_length,) = unpack('!H',data)
    my_file.write(f'Payload_length: {payload_length}\n')
    #print(f'type: {type(payload_length)}')
    #print(f'payload_length: {payload_length}')


    # Skip if it is not data message
    if msg_type != b'1': #0x31:
      print(f'This is not data message!!')

      # Get entire payload
      payload = s.recv(payload_length, socket.MSG_WAITALL)
      ##
      my_file.write('Header_payload: \n')
      my_file.write(str(payload))
      continue#pass#print(f'Skip Message type {msg_type}')

    # Process data message
    else:
        
      # Get header chunk
      data = s.recv(4, socket.MSG_WAITALL)
      ##
      my_file.write('Data: \n')
      my_file.write(str(data))
      (header_chunk_type, header_version, header_chunk_size,) = unpack('!cBH',data)
      ##
      my_file.write(f'header_chunk_type: {header_chunk_type} ; header_version: {header_version}\n')
      my_file.write(f'header_chunk_size: {header_chunk_size}\n')
	
      # Skip header chunk
      data = s.recv(header_chunk_size, socket.MSG_WAITALL)
      ##
      my_file.write('Data: \n')
      my_file.write(str(data))

      # Process data chunk
      data = s.recv(4, socket.MSG_WAITALL)
      (data_chunk_type, data_version, data_chunk_size,) = unpack('!cBH',data)
      ##
      my_file.write('Data: \n')
      my_file.write(str(data))
      my_file.write(f'data_chunk_type: {data_chunk_type} ; data_version: {data_version}\n')
      my_file.write(f'data_chunk_size: {data_chunk_size}\n')

      # Get data info
      data = s.recv(8, socket.MSG_WAITALL)
      (sample_id, num_channels, data_format, data_point) = unpack('!IBbH',data)
      ##
      my_file.write('Data: \n')
      my_file.write(str(data))
      my_file.write(f'sample_id: {sample_id} ; num_channels: {num_channels}\n')
      my_file.write(f'data_format: {data_format} ; data_point: {data_point}\n')

      # Calculate data size (bytes)
      data_size = data_point * 3 * 1 # 24bits = 3 bytes, 1 channel

      # Get data
      data = s.recv(data_size, socket.MSG_WAITALL)
      print('Recieved:', data) 
      print(f'len:  {str(len(data))}') #196500
      #my_file.write(str(data))
      print(sample_id, num_channels, data_format) #1090519052 94 100
      print(data_point) #65500
      print(data_size)  #196500
      #my_file.write('Data: \n')
      #my_file.write(str(data))

      # Process data
      array = bytearray(data)
      for i in range(0,len(array),3):
        msg = array[i:i+3]
        print(f'{msg}')
        one,two,three = unpack('BBb', msg)
        hexa_file.write(f'{one},{two},{three}\n')
        bits = one + two*256 + three*256*256
        #if bits > 8388607:
        #  bits = bits - 8388607
        volt=bits*6/16777216
        print(f'{volt}')
        volt_file.write(f'{volt}\n')
      a=a+1

s.close()
my_file.close()
volt_file.close()
hexa_file.close()
