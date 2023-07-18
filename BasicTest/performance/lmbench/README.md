# lmbench

lmbench 是个用于评价系统综合性能的多平台开源 benchmark，能够测试包括文档读写、内存操作、进程创建销毁开销、网络等性能，测试方法简单。

## 文件树

```
lmbench
├── log #测试日志与结果
│   ├── images
│   │   ├── percent-diff.png
│   │   └── summary-diff.png
│   ├── LicheeRVD1
│   │   ├── LicheeRVD1.log
│   │   ├── openeuler-riscv64.0
│   │   ├── percent.errs
│   │   ├── percent.out
│   │   ├── summary.errs
│   │   └── summary.out
│   ├── NezhaD1
│   │   ├── NezhaD1.log
│   │   ├── openeuler-riscv64.0
│   │   ├── percent.errs
│   │   ├── percent.out
│   │   ├── summary.errs
│   │   └── summary.out
│   ├── QEMU
│   │   ├── openeuler-riscv64.0
│   │   ├── percent.errs
│   │   ├── percent.out
│   │   ├── QEMU.log
│   │   ├── QEMU-dmesg.log
│   │   ├── summary.errs
│   │   └── summary.out
│   ├── Unmatched
│   │   ├── openeuler-riscv64.0
│   │   ├── percent.errs
│   │   ├── percent.out
│   │   ├── summary.errs
│   │   ├── summary.out
│   │   ├── Unmatched.log
│   │   └── Unmatched-dmesg.log
│   ├── VisionFive1
│   │   ├── openeuler-riscv64.0
│   │   ├── percent.errs
│   │   ├── percent.out
│   │   ├── summary.errs
│   │   ├── summary.out
│   │   ├── VisionFive1.log
│   │   └── VisionFive1-dmesg.log
│   ├── VisionFive2
│   │   ├── openeuler-riscv64.0
│   │   ├── percent.errs
│   │   ├── percent.out
│   │   ├── summary.errs
│   │   ├── summary.out
│   │   └── VisionFive2.log
│   └── x86_64
│       ├── Makefile
│       ├── percent.errs
│       ├── percent.out
│       ├── summary.errs
│       ├── summary.out
│       └── x86_64-linux-gnu
│           └── localhost.localdomain.0
├── method.md   #测试方法
├── README.md   #测试说明
└── result.md   #测试结果
```