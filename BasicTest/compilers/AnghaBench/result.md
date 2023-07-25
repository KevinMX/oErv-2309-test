# AnghaBench 测试报告

## 概述

AnghaBench 包含了一百万个可编译的 C 文件，可用于对 C 编译器进行编译测试，验证编译器本身性能，以及查找编译器错误。

## 测试环境

- 发行版版本：openEuler 23.03 RISC-V Preview V1
- 虚拟机版本：QEMU 7.2.0

## 测试方法

见 [method.md](./method.md)。

## 测试结果

```
Total: 1044021 Passed: 1042280 Failed: 1741
```

通过率 99.83%

详细日志见 [AnghaBench.log](./log/AnghaBench.log.gz)

失败样例的编译器信息见 [compilation_log.tar.gz](./log/compilation_log.tar.gz)

### 失败样例分析

> 判定原因&具体数据

#### 平台相关的代码编译失败

失败原因如下。详细列表见 [arch.md](./log/arch.md)。

不支持 RISC-V 平台的条件编译：

```
./darwin-xnu/osfmk/vm/extr_vm_shared_region.c_vm_commpage_text_init.c: In function ‘vm_commpage_text_init’:
./darwin-xnu/osfmk/vm/extr_vm_shared_region.c_vm_commpage_text_init.c:70:2: error: #error Unknown architecture.
   70 | #error Unknown architecture.
```

非 RISC-V 架构的内联汇编：

```
./Quake-III-Arena/code/qcommon/extr_vm_ppc.c_AsmCall.c: Assembler messages:
./Quake-III-Arena/code/qcommon/extr_vm_ppc.c_AsmCall.c:17: Error: unrecognized opcode `lwz r12,0(r4)'
./Quake-III-Arena/code/qcommon/extr_vm_ppc.c_AsmCall.c:18: Error: illegal operands `addi r4,r4,-4'
./Quake-III-Arena/code/qcommon/extr_vm_ppc.c_AsmCall.c:19: Error: unrecognized opcode `cmpwi r12,0'
./Quake-III-Arena/code/qcommon/extr_vm_ppc.c_AsmCall.c:20: Error: unrecognized opcode `bc 12,0,systemTrap'
```

共 1170 项

#### AnghaBench 样例的代码缺陷

如下，使用了不标准的语法或存在未定义的类型。列表见 [testcase\_problem.md](./log/testcase_problem.md)

共 132 项

#### 其他

439 项。

### 测试结论

AnghaBench 测试通过。测试中出现的问题为架构不支持或测试用例本身问题，非编译器本身问题。