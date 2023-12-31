# csmith 测试报告

## 概述

Csmith 是 C 程序的随机生成器。它的主要目的是使用差异测试作为测试预言，使用随机程序查找编译器错误。

## 测试环境

- 发行版版本：openEuler 23.03 RISC-V Preview V1
- 虚拟机版本：QEMU ≥ 8.0

## 测试方法

见 [method.md](./method.md)。

## 测试结果

测试性运行 100 个测试用例的结果可查看 [csmith.log](./log/csmith.log)，使用 csmith 自带的脚本进行自动化测试。为了测试所需时间，添加了 `time` 指令。

测试结果：100 个测试用例均通过，但在未做并行化处理的前提下，耗时 112 分钟。如按照社区测试能力执行指南要求执行百万级测试用例，所需时间过久。

## 测试结论

由于测试执行速度过慢，测试用例数量不足，暂未测出编译器存在问题。