# fio 测试报告

## 概述

`fio` 是测试 IOPS 的工具，用来对磁盘进行压力测试和验证。磁盘 IO 是检查磁盘性能的重要指标，可以按照负载情况分成顺序读写、随机读写两大类。`fio` 是一个可以产生很多线程或进程并执行用户指定的特定类型I/O操作的工具，`fio` 的典型用法是编译和模拟的I/O负载匹配的作业文件。也就是说 `fio` 是一个多线程 IO 生成工具，可以生成多种 IO 模式，用来测试磁盘设备的性能（也包括文件系统：如针对网络文件系统 NFS 的 IO 测试）

## 测试环境

- 发行版版本：openEuler 23.03 RISC-V Preview V1
- 内核版本：6.1.19
- 虚拟机版本：QEMU 8.0.2

### 与上游测试方式不同之处

- `fio` 从软件源直接获取而不是编译安装。
- 测试目录更改为当前目录下的 `test` 而不是创建新的文件系统执行。
- 测试文件大小改为 1G。

## 测试方法

见 [method.md](./method.md)。

## 测试结果

除了两块采用全志 D1 的开发板（荔枝派和哪吒）无法运行外，测试通过。QEMU 下 IO 性能表现良好。

测试结果详见 [log](./log) 目录下的日志文件。

### 测试结果对比表

| 测试类型      | 块大小     | 测试结果                                          |
|-----------|---------|-----------------------------------------------|
| read      | 4096B   | [r=56.9MiB/s][r=14.6k IOPS]                   |
| read      | 16.0KiB | [r=217MiB/s][r=13.9k IOPS]                    |
| read      | 32.0KiB | [r=267MiB/s][r=8543 IOPS]                     |
| read      | 64.0KiB | [r=586MiB/s][r=9377 IOPS]                     |
| read      | 128KiB  | [r=849MiB/s][r=6794 IOPS]                     |
| read      | 256KiB  | [r=838MiB/s][r=3350 IOPS]                     |
| read      | 512KiB  | [r=675MiB/s][r=1350 IOPS]                     |
| read      | 1024KiB | [r=576MiB/s][r=576 IOPS]                      |
| write     | 4096B   | [w=45.4MiB/s][w=11.6k IOPS]                   |
| write     | 16.0KiB | [w=182MiB/s][w=11.6k IOPS]                    |
| write     | 32.0KiB | [w=90.2MiB/s][w=2885 IOPS]                    |
| write     | 64.0KiB | [w=407MiB/s][w=6515 IOPS]                     |
| write     | 128KiB  | [w=580MiB/s][w=4640 IOPS]                     |
| write     | 256KiB  | [w=796MiB/s][w=3183 IOPS]                     |
| write     | 512KiB  | [w=739MiB/s][w=1477 IOPS]                     |
| write     | 1024KiB | [w=731MiB/s][w=730 IOPS]                      |
| randread  | 4096B   | [r=49.7MiB/s][r=12.7k IOPS]                   |
| randread  | 16.0KiB | [r=200MiB/s][r=12.8k IOPS]                    |
| randread  | 32.0KiB | [r=224MiB/s][r=7183 IOPS]                     |
| randread  | 64.0KiB | [r=728MiB/s][r=11.6k IOPS]                    |
| randread  | 128KiB  | [r=822MiB/s][r=6579 IOPS]                     |
| randread  | 256KiB  | [r=731MiB/s][r=2922 IOPS]                     |
| randread  | 512KiB  | [r=782MiB/s][r=1563 IOPS]                     |
| randread  | 1024KiB | [r=698MiB/s][r=698 IOPS]                      |
| randwrite | 4096B   | [w=46.6MiB/s][w=11.9k IOPS]                   |
| randwrite | 16.0KiB | [w=185MiB/s][w=11.9k IOPS]                    |
| randwrite | 32.0KiB | [w=150MiB/s][w=4808 IOPS]                     |
| randwrite | 64.0KiB | [w=473MiB/s][w=7571 IOPS]                     |
| randwrite | 128KiB  | [w=428MiB/s][w=3425 IOPS]                     |
| randwrite | 256KiB  | [w=921MiB/s][w=3683 IOPS]                     |
| randwrite | 512KiB  | [w=755MiB/s][w=1509 IOPS]                     |
| randwrite | 1024KiB | [w=655MiB/s][w=654 IOPS]                      |
| randrw    | 4096B   | [r=34.6MiB/s,w=14.5MiB/s][r=8862,w=3706 IOPS] |
| randrw    | 16.0KiB | [r=134MiB/s,w=56.3MiB/s][r=8560,w=3604 IOPS]  |
| randrw    | 32.0KiB | [r=208MiB/s,w=88.7MiB/s][r=6659,w=2838 IOPS]  |
| randrw    | 64.0KiB | [r=397MiB/s,w=165MiB/s][r=6353,w=2637 IOPS]   |
| randrw    | 128KiB  | [r=672MiB/s,w=281MiB/s][r=5372,w=2251 IOPS]   |
| randrw    | 256KiB  | [r=671MiB/s,w=298MiB/s][r=2682,w=1192 IOPS]   |
| randrw    | 512KiB  | [r=506MiB/s,w=224MiB/s][r=1012,w=448 IOPS]    |
| randrw    | 1024KiB | [r=459MiB/s,w=215MiB/s][r=458,w=215 IOPS]     |
