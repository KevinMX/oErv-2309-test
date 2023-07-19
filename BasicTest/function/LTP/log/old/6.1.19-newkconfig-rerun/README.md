# LTP 测试

LTP 测试套件包含一组用于测试 Linux 内核和相关功能的工具。我们的目标是通过将测试自动化引入测试工作来改进 Linux 内核和系统库。

使用 Linux Test Project（简称 LTP）对内核进行测试。本次测试使用的 LTP 版本为 [20230127](https://github.com/linux-test-project/ltp/releases/tag/20230127)。使用的内核是经过修复的 [kernel-6.1.19-0.0.0.0.oe2303.riscv64.rpm](http://obs-backend.tarsier-infra.com:82/home:/laokz:/branches:/openEuler:/23.03/23.02/riscv64/kernel-6.1.19-0.0.0.0.oe2303.riscv64.rpm)。

## 安装修订版本内核

启动原虚拟机，在虚拟机内使用 `rpm -i` 解压新内核，将 `/boot/vmlinuz` 拷贝到宿主机。关机，`gunzip` 解压缩 `vmlinuz` ，修改 `qemu` 参数 `-kernel=vmlinuz` ，添加 `-append "root=/dev/vda2"`，移除 `-bios`，再启动。

## 测试结果

- 测试用例总数：2379
- 通过（`Result` 字段标记为 `PASS`）：2096
- 跳过的（`Result` 字段标记为 `CONF`）：249
- 失败的（`Result` 字段标记为 `FAIL`）：34
- 内核版本：6.1.19-0.0.0.0.oe2303.riscv64
- 计算机架构：riscv64
- 主机名称：openeuler-riscv64

## 失败结果评估

整理测试日志，得到结果分析文件 [res.csv](./res.csv)。

## 日志

附有此次 LTP 测试产生的 `output` 目录和 `results` 目录。

- `results/LTP_RUN_ON-2023_05_06-16h_33m_50s.log`：测试结果统计。
- `output/LTP_RUN_ON-tests.output.failed` 失败测试的名字（tag）及具体命令。
- `output/LTP_RUN_ON-tests.output.tconf`：（可能）需要调整配置的测试名（tag）及具体命令，包括且大部分为主动跳过的测试。
- `output/tests.output.zst`：所有测试的日志，因原文件过大，故使用 Zstd 压缩。
- `output/cpuctl_results_stress-*.txt`：从文件名上看，似乎为进行 CPU 相关测试时产生的输出，但是这几个文件都只有一行日期。