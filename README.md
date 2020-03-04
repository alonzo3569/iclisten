# iclisten

## icListen Channels
* Command & control channel: 
  * UDP: port 62726
  * Msgs sent to iclisten __cannot__ exceed __100 bytes__
  * Little endian (LSB)
  * binary format
  
* Streaming channels: 
  * UDP: port 62726
  * Msgs length 32bits ?
  * Big endian (MSB)
  * binary format

Data Type | TCP | UDP 
:--- | :--- | :---
Time Series | 51678 | 51676
Spectrum | 51679 | 51677
Epoch Msgs | 51680 
Other Sensors | 51681

  
## TCP v.s. UDP
* UDP header: 8 bytes
* TCP header: 20 bytes
