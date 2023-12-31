# fio

`fio` 是测试 IOPS 的工具，用来对磁盘进行压力测试和验证。磁盘 IO 是检查磁盘性能的重要指标，可以按照负载情况分成顺序读写、随机读写两大类。`fio` 是一个可以产生很多线程或进程并执行用户指定的特定类型I/O操作的工具，`fio` 的典型用法是编译和模拟的I/O负载匹配的作业文件。也就是说 `fio` 是一个多线程 IO 生成工具，可以生成多种 IO 模式，用来测试磁盘设备的性能（也包括文件系统：如针对网络文件系统 NFS 的 IO 测试）

## 与上游测试方式不同之处

- `fio` 从软件源直接获取而不是编译安装。
- 测试目录更改为当前目录下的 `test` 而不是创建新的文件系统执行。
- 测试文件大小改为 1G。

## 文件树

fio
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