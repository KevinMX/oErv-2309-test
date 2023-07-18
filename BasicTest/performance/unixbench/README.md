# unixbench

Unixbench 是一个类 unix 系统下的开源性能测试工具，被广泛用于测试 Linux 系统主机的综合性能，测试结果不仅依赖硬件配置（CPU/内存/硬盘），还取决于操作系统、库甚至编译器的差异。既可以评估单进程性能，也可以评估多进程性能。

## 与上游测试方式不同之处

- `unixbench` 直接拉取 GitHub 主线最新源码。
- 未修改最大线程数。

## 文件树

```
unixbench
├── log
│   ├── LecheeRVD1.log
│   ├── NezhaD1.log
│   ├── QEMU.log
│   ├── Unmatched.log
│   ├── VisionFive1.log
│   └── VisionFive2.log
├── method.md   #测试方法
├── README.md   #测试说明
└── result.md   #测试结果
```