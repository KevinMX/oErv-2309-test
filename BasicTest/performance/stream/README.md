# stream

stream 是通过对数组的 copy，scale，add，triad 操作来测试 CPU 的内存访问带宽和浮点运算能力。Copy为最简单的操作，即从一个内存单元中读取一个数，并复制到另一个内存单元，有2次访存操作。Scale是乘法操作，从一个内存单元中读取一个数，与常数Scale相乘，得到的结果写入另一个内存单元，有2次访存。Add是加法操作，从两个内存单元中分别读取两个数，将其进行加法操作，得到的结果写入另一个内存单元中，有2次读和1次写共3次访存。Triad是前面三种的结合，先从内存中读取一个数，与scale相乘得到一个乘积，然后从一个内存单元中读取一个数与之前的乘积相加，得到的结果再写入内存，所以，有2次读和1次写共三次访存操作。

## 文件树

```
stream
├── log
│   ├── LicheeRVD1.log
│   ├── NezhaD1.log
│   ├── QEMU.log
│   ├── Unmatched.log
│   ├── VisionFive1.log
│   └── VisionFive2.log
├── method.md   #测试方法
├── README.md   #测试说明
└── result.md   #测试结果
```