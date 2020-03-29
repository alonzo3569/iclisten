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

## Reference
* [__計算機編碼__][0]
* [__有號數字表示法(2's,1's)__][1]
* __Python binary :__
  * [__pynote 1429__][2]
  * [__pynote 1383__][3]
  * [__Python 運算子__][4]
  * [__Python 二進位運算__][5]
* __原碼、反碼、補碼 :__
  * [__pdf__][6]
  * [__link1__][7]
  * [__link2__][8]
  * [__link3__][9]
  * [__link4__][10]
  * [__link5__][11]
  * [__Wiki 2's__][12]
  * [__Wiki 1's__][13]
  * [__Wiki signed number representations__][14]


[0]: https://hackmd.io/@sysprog/binary-representation
[1]: https://notfalse.net/20/signed-number-representations
[2]: https://www.pynote.net/archives/1429
[3]: https://www.pynote.net/archives/1383
[4]: https://www.footmark.info/programming-language/python/python-operator/
[5]: https://www.jianshu.com/p/3a31065a8e58
[6]: http://www2.lssh.tp.edu.tw/~jinghuei/resource/3%E6%95%B8%E5%AD%97%E7%B3%BB%E7%B5%B1%E8%88%87%E8%B3%87%E6%96%99%E8%A1%A8%E7%A4%BA%E6%B3%95.pdf
[7]: https://read01.com/zh-tw/g5eQPe.html#.XoDTMGgzaUm
[8]: https://read01.com/6mEBD8.html#.Xm8XG2gzaUl
[9]: https://read01.com/0aG3PB.html#.Xm8XGmgzaUl
[10]: https://read01.com/0aGLAB.html#.XoDGkWgzaUl
[11]: https://www.cnblogs.com/zhangziqiu/archive/2011/03/30/ComputerCode.html
[12]: https://zh.wikipedia.org/wiki/%E4%BA%8C%E8%A3%9C%E6%95%B8
[13]: https://zh.wikipedia.org/wiki/%E4%B8%80%E8%A3%9C%E6%95%B8
[14]: https://zh.wikipedia.org/wiki/%E6%9C%89%E7%AC%A6%E8%99%9F%E6%95%B8%E8%99%95%E7%90%86
