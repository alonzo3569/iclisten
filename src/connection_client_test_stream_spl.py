# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 12:07:30 2020

@author: logan
"""

## socket pkg
import socket
from struct import pack, unpack

## plot pkg
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

## math pkg
from math import sqrt, log

## SPL params
#previous_volt = 0
sen = -171.1
peak_volt_list=[]
def average(num_list):
    num_sum=0
    for i in range(len(num_list)):
        num_sum += num_list[i]
    return num_sum/len(num_list)
    

## plot params
current_frame = [0 for i in range(500000)] #200000
previous_frame = [0 for i in range(500000)]
volt_list=[]
plt.figure()
plt.ion()

## socket params
HOST = '192.168.1.109'
PORT = 51678               # Cammand 62726 ; Time Series(TCP) 51678 ; 
			   # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


## Setup connection
s = socket.socket()        # socket.SOCK_DGRAM: UDP ; socket.SOCK_STREAM: TCP
s.connect((HOST, PORT))

# Sending Start stream message
msg=b'\x33\x2a\x00\x04\x00\x00\x00\x00'
s.send(msg)
my_file = open('./data.txt','w')
volt_file = open('./volt_msg.txt','w')
hexa_file = open('./hexa_msg.txt','w')
frame_file = open('./frame_msg.txt','w')
a = 1

while a<10000000000:


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
      #print('Recieved:', data) 
      #print(f'len:  {str(len(data))}') #196500
      #my_file.write(str(data))
      #print(sample_id, num_channels, data_format) #1090519052 94 100
      #print(data_point) #65500
      #print(data_size)  #196500
      #my_file.write('Data: \n')
      #my_file.write(str(data))

      # Process data
      array = bytearray(data)
      for i in range(0,len(array),3):
        # Convert bytes to volts 
        msg = array[i:i+3]
        #print(f'msg: {msg}')
        one,two,three = unpack('BBb', msg)
        hexa_file.write(f'one,two,three: {one},{two},{three}\n')
        bits = one + two*256 + three*256*256
        volt = bits*6/16777216
        #print(f'{volt}')

        # Write volt to file
        volt_file.write(f'{volt}\n')

        # Append volt to volt_list
        volt_list.append(volt) 


      # Calculate SPL
      for i in range(1,len(volt_list)-1): # i=1~40 len(volt_list)=42

        # Find peak voltage
        if volt_list[i] > volt_list[i-1] and volt_list[i] > volt_list[i+1] and volt_list[i] > 0:
	  # This is peak value
	  # Save peak volt (write to file)
          #print(f'Peak volt: {volt_list[i]}')
          peak_volt_list.append(volt_list[i])

	  # Calculate rms
	  #rms_volt = volt_list[i]/sqrt(2)
	  # Calculate SPL
	  #spl =  20 * log(volt_list[i],10) - sen
	  # print spl and save spl
	  #print(f'{spl}')  

      # Calculate average peak volt 
      avg_peak_volt = average(peak_volt_list)

      # Calculate SPL
      spl =  20 * log(avg_peak_volt/sqrt(2),10)  - sen
      # print spl and save spl
      if a%100 == 0:
        print(f'SPL: {spl}')           
      a=a+1

#plt.ioff()
#plt.show(block=False)
s.close()
my_file.close()
volt_file.close()
hexa_file.close()
frame_file.close()
