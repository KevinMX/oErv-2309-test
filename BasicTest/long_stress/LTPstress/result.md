# LTP Stress 测试报告

## 概述

Linux Test Project / LTP 中的 stress 组件可用于对内核进行压稳测试。

## 测试环境

- 发行版版本：openEuler 23.03 RISC-V Preview V1
- 内核版本：6.1.19
- 虚拟机版本：QEMU 8.0.2
- 宿主机：Arch Linux on WSL 2
- 软件版本：LTP 20230516 release ([GitHub](https://github.com/linux-test-project/ltp/releases/tag/20230516))

## 测试方法 

见 [method.md](./method.md)。

## 测试结果

内核有报错（会出现 SIG 7 / SIG 11），系统依旧正常响应，未出现死锁等情况。

[日志文件](./log/ltpstress.tar.zst)较大，已打包压缩，请解压后查看。