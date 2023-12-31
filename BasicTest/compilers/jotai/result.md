# jotai 测试报告

## 概述

jotai 是从 AnghaBench 中抽取修改的可编译可运行的代码测试集。

## 测试环境

- 发行版版本：openEuler 23.03 RISC-V Preview V1
- 虚拟机版本：QEMU ≥ 8.0

## 测试方法

见 [method.md](./method.md)。

## 测试结果

对 `anghaLeaves` 进行测试时的日志包含在 [test.log.gz](./log/test.log.gz) 文件中。

- anghaLeaves 中失败测试列表：[anghaLeaves.fail](./log/anghaLeaves.fail)
- anghaMath 中失败测试列表：[anghaMath.fail](./log/anghaMath.fail)

### History

先前不完整的 jotai 测试结果包含在 old 目录中。

### AnghaLeaves

643 项失败。

#### 命名冲突

测试代码中的枚举或符号在系统头文件中已经定义为宏或以不同的类型声明过了。

```
extr_darwin-xnubsdmiscfsdevfsdevfs_fdesc_support.c_fdesc_pathconf_Final.c
extr_darwin-xnubsdmiscfsfifofsfifo_vnops.c_fifo_pathconf_Final.c
extr_linuxarchx86kvmpmu_amd.c_msr_to_index_Final.c
```

#### 类型定义冲突

测试代码中的存在对 `uint16_t` 等类型的定义，但是与系统 libc 的定义不同。

类别包含了所有未列出的失败项目。

#### 平台相关代码

测试代码中存在对架构相关的预定义宏的使用，然而 RISC-V 架构不被包含在可识别的
列表中。

```
extr_linuxfslibfs.c_simple_statfs_Final.c:
```

#### 未定义的符号

代码中使用的符号/宏未定义。

```
extr_darwin-xnuosfmki386machine_routines.c_ml_static_ptovirt_Final.c
```

## 测试结论

jotai 测试中出现的错误均与编译器本身无关，编译器本身质量良好。