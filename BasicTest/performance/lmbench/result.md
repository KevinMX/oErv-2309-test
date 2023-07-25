# lmbench 性能测试报告

## 概述

`lmbench` 是个用于评价系统综合性能的多平台开源 benchmark，能够测试包括文档读写、内存操作、进程创建销毁开销、网络等性能，测试方法简单。

## 测试环境

- 发行版版本：openEuler 23.03 RISC-V Preview V1
- 内核版本：6.1.19
- 虚拟机版本：QEMU 8.0.2

## 测试方法

见 [method.md](./method.md)

## 测试结果

测试通过，但运行部分项目时内核日志有报错，不影响测试运行与结果。

测试结果详见对应目录下的日志文件。

QEMU 下的详细测试结果

```
                 L M B E N C H  3 . 0   S U M M A R Y
                 ------------------------------------
		 (Alpha software, do not distribute)


Context switching - times in microseconds - smaller is better
-------------------------------------------------------------------------
Host                 OS  2p/0K 2p/16K 2p/64K 8p/16K 8p/64K 16p/16K 16p/64K
                         ctxsw  ctxsw  ctxsw ctxsw  ctxsw   ctxsw   ctxsw
--------- ------------- ------ ------ ------ ------ ------ ------- -------
openeuler Linux 6.1.19-   59.9   62.0   61.2   74.4   75.5    80.9    86.1

*Local* Communication latencies in microseconds - smaller is better
---------------------------------------------------------------------
Host                 OS 2p/0K  Pipe AF     UDP  RPC/   TCP  RPC/ TCP
                        ctxsw       UNIX         UDP         TCP conn
--------- ------------- ----- ----- ---- ----- ----- ----- ----- ----
openeuler Linux 6.1.19-  59.9            316.2       294.6       394.

File & VM system latencies in microseconds - smaller is better
-------------------------------------------------------------------------------
Host                 OS   0K File      10K File     Mmap    Prot   Page   100fd
                        Create Delete Create Delete Latency Fault  Fault  selct
--------- ------------- ------ ------ ------ ------ ------- ----- ------- -----
openeuler Linux 6.1.19-  208.0  159.6  559.0  231.7  875.3K                    

*Local* Communication bandwidths in MB/s - bigger is better
-----------------------------------------------------------------------------
Host                OS  Pipe AF    TCP  File   Mmap  Bcopy  Bcopy  Mem   Mem
                             UNIX      reread reread (libc) (hand) read write
--------- ------------- ---- ---- ---- ------ ------ ------ ------ ---- -----
openeuler Linux 6.1.19- 105. 178. 297.  381.5 6047.5 3239.4 2048.8 2978 3063.

Memory latencies in nanoseconds - smaller is better
    (WARNING - may not be correct, check graphs)
------------------------------------------------------------------------------
Host                 OS   Mhz   L1 $   L2 $    Main mem    Rand mem    Guesses
--------- -------------   ---   ----   ----    --------    --------    -------
openeuler Linux 6.1.19-  8988 2.6290 3.5840   26.1       139.1

```

与 openEuler 23.03 x86_64 执行 lmbench 时程序输出的错误日志进行了对比，注意到 RISC-V 平台出现的报错在 x86_64 均有出现，没有出现 RISC-V 平台特有的错误，对比结果见下图。x86_64 平台下的测试结果位于 [x86_64](./log/x86_64/) 目录中，仅供参考。

左：openEuler 23.03 x86_64，右：openEuler 23.03 RISC-V on QEMU

![percent](./log/images/percent-diff.png)

![summary](./log/images/summary-diff.png)