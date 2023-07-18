# csmith

csmith 是适用于编译器的冒烟测试工具，能够生成大量合法的 C 文件作为测试用例，进而测试 C 编译器的标准性。

> 要求的样本量过于庞大（百万量级），测试所需时间不现实。

## 文件树
```
csmith
├── log
│   └── csmith.log
├── method.md   #测试方案
├── README.md   #测试说明
├── result.md   #测试结果分析
└── src #测试代码
    ├── csrc.mk
    ├── epoch.sh
    ├── list.mk
    └── makefile
```