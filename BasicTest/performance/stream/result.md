# stream 测试报告

## 概述

stream 是通过对数组的 copy，scale，add，triad 操作来测试 CPU 的内存访问带宽和浮点运算能力。Copy为最简单的操作，即从一个内存单元中读取一个数，并复制到另一个内存单元，有2次访存操作。Scale是乘法操作，从一个内存单元中读取一个数，与常数Scale相乘，得到的结果写入另一个内存单元，有2次访存。Add是加法操作，从两个内存单元中分别读取两个数，将其进行加法操作，得到的结果写入另一个内存单元中，有2次读和1次写共3次访存。Triad是前面三种的结合，先从内存中读取一个数，与scale相乘得到一个乘积，然后从一个内存单元中读取一个数与之前的乘积相加，得到的结果再写入内存，所以，有2次读和1次写共三次访存操作。

## 测试环境

- 发行版版本：openEuler 23.03 RISC-V Preview V1
- 内核版本：6.1.19
- 虚拟机版本：QEMU 8.0.2

## 测试方法

见 [method.md](./method.md)

## 测试结果

测试通过。测试结果详见 [log](./log) 下的日志文件；QEMU 结果如下。

```
-------------------------------------------------------------
STREAM version $Revision: 5.10 $
-------------------------------------------------------------
This system uses 8 bytes per array element.
-------------------------------------------------------------
Array size = 10000000 (elements), Offset = 0 (elements)
Memory per array = 76.3 MiB (= 0.1 GiB).
Total memory required = 228.9 MiB (= 0.2 GiB).
Each kernel will be executed 10 times.
 The *best* time for each kernel (excluding the first iteration)
 will be used to compute the reported bandwidth.
-------------------------------------------------------------
Number of Threads requested = 8
Number of Threads counted = 8
-------------------------------------------------------------
Your clock granularity/precision appears to be 1 microseconds.
Each test below will take on the order of 22462 microseconds.
   (= 22462 clock ticks)
Increase the size of the arrays if this shows that
you are not getting at least 20 clock ticks per test.
-------------------------------------------------------------
WARNING -- The above is only a rough guideline.
For best results, please be sure you know the
precision of your system timer.
-------------------------------------------------------------
Function    Best Rate MB/s  Avg time     Min time     Max time
Copy:           23081.3     0.007845     0.006932     0.008717
Scale:          10794.8     0.018168     0.014822     0.020507
Add:            13298.5     0.021114     0.018047     0.023301
Triad:          10068.4     0.026150     0.023837     0.029336
-------------------------------------------------------------
Solution Validates: avg error less than 1.000000e-13 on all three arrays
-------------------------------------------------------------
```