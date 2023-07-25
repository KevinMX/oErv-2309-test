# UnixBench 测试报告

## 概述

Unixbench 是一个类 unix 系统下的开源性能测试工具，被广泛用于测试 Linux 系统主机的综合性能，测试结果不仅依赖硬件配置（CPU/内存/硬盘），还取决于操作系统、库甚至编译器的差异。既可以评估单进程性能，也可以评估多进程性能。

## 测试环境

- 发行版版本：openEuler 23.03 RISC-V Preview V1
- 内核版本：6.1.19
- 虚拟机版本：QEMU 8.0.2

## 测试方法

见 [method.md](./method.md)

### 与上游测试方式不同之处

- `unixbench` 直接拉取 GitHub 主线最新源码。
- 未修改最大线程数。

## 测试结果

测试通过。测试结果详见 [log](./log) 目录下的日志文件。

| QEMU  | NezhaD1 | LicheeRVD1 | Unmatched | VisionFive1 | VisionFive2 |
|-------|---------|------------|-----------|-------------|-------------|
| 230.4 | 104.1   | 103.1      | 733.8     | 367.8       | 1318.1      |

QEMU 平台的详细测试结果如下：

```
8 CPUs in system; running 8 parallel copies of tests

Dhrystone 2 using register variables       20449485.9 lps   (10.1 s, 7 samples)
Double-Precision Whetstone                     4876.5 MWIPS (10.1 s, 7 samples)
Execl Throughput                                301.2 lps   (29.6 s, 2 samples)
File Copy 1024 bufsize 2000 maxblocks         91327.7 KBps  (30.0 s, 2 samples)
File Copy 256 bufsize 500 maxblocks           23040.9 KBps  (30.0 s, 2 samples)
File Copy 4096 bufsize 8000 maxblocks        332662.0 KBps  (30.0 s, 2 samples)
Pipe Throughput                              126947.2 lps   (10.1 s, 7 samples)
Pipe-based Context Switching                  28651.2 lps   (10.1 s, 7 samples)
Process Creation                               1751.8 lps   (30.2 s, 2 samples)
Shell Scripts (1 concurrent)                    619.8 lpm   (60.4 s, 2 samples)
Shell Scripts (8 concurrent)                     85.5 lpm   (62.8 s, 2 samples)
System Call Overhead                         791249.9 lps   (10.2 s, 7 samples)

System Benchmarks Index Values               BASELINE       RESULT    INDEX
Dhrystone 2 using register variables         116700.0   20449485.9   1752.3
Double-Precision Whetstone                       55.0       4876.5    886.6
Execl Throughput                                 43.0        301.2     70.1
File Copy 1024 bufsize 2000 maxblocks          3960.0      91327.7    230.6
File Copy 256 bufsize 500 maxblocks            1655.0      23040.9    139.2
File Copy 4096 bufsize 8000 maxblocks          5800.0     332662.0    573.6
Pipe Throughput                               12440.0     126947.2    102.0
Pipe-based Context Switching                   4000.0      28651.2     71.6
Process Creation                                126.0       1751.8    139.0
Shell Scripts (1 concurrent)                     42.4        619.8    146.2
Shell Scripts (8 concurrent)                      6.0         85.5    142.6
System Call Overhead                          15000.0     791249.9    527.5
                                                                   ========
System Benchmarks Index Score                                         230.4
```

## 测试结论

系统性能表现良好，符合预期。