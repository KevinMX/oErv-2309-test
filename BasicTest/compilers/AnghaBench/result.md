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

失败样例的编译器信息见 [compilation\_log.tar.gz](./log/compilation_log.tar.gz)

### 失败样例分析

#### 平台相关的代码编译失败

如非 RISC-V 架构的内联汇编，不支持 RISC-V 平台的条件编译，列表见
[arch.md](./arch.md)。

共 1170 项

#### AnghaBench 样例的代码缺陷

如使用了不标准的语法或存在未定义的类型。列表见
[testcase\_problem.md](./testcase\_problem.md)

共 132 项

#### 其他

439 项。

### 测试结论

AnghaBench 测试通过。