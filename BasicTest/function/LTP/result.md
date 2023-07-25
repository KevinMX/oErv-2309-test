# LTP 测试报告

## 概述

LTP 是由 SGI, OSDL 和 Bull 联合开发的项目，并由 IBM, Cisco, Fujitsu, SUSE, Red Hat, Oracle 和其他维护，其目的是向开源社区提供用于验证 Linux 可靠性、健壮性和稳定性的测试套件。

## 测试环境

- 发行版版本：openEuler 23.03 RISC-V Preview V1
- 虚拟机版本：QEMU ≥ 8.0

## 测试方法

见 [method.md](./method.md)。

## 测试结果

- 测试用例总数：2379
- 跳过的：308
- 失败的：31

将超时的失败的用例进行重新测试，整理测试日志，得到如下结果。

- leapsec01.c:84: TBROK: adjtimex status 8208 not set：系统默认开启了时钟同步服务，停止 systemd-timesyncd.service 后可通过
- clock_settime03: 同上，关闭时钟同步后复测通过
- getxattr04: tst_test.c:1107: TBROK: mount(/dev/vdc1, mntpoint, xfs, 0, (nil)) failed: ENODEV (19)：内核未开启 xattr 相关选项
- fanotify10: TCONF: fanotify is not configured in this kernel：内核未开启 fanotify
- keyctl03: keyctl03.c:31: TBROK: Failed to add key：内核默认未开启相关选项
- setfsuid02_16: setfsuid02.c:26: TBROK: uid -1 of invalid_uid is too large for testing 16-bit version of setfsuid()：测试用例问题
- perf_event_open01: perf_event_open01    1  TFAIL  :  perf_event_open01.c:156: perf_event_open PERF_COUNT_HW_INSTRUCTIONS failed unexpectedly: TEST_ERRNO=EINVAL(22): Invalid argument：QEMU 环境下不支持
- vma05: vma05 1 TFAIL: [vdso] bug not patched：见 https://github.com/linux-test-project/ltp/issues/477 ，测试用例本身问题
- irqbalance01: irqbalance01.c:287: TFAIL: Heuristic: Detected 0 irq-cpu pairs have been dissallowed：默认未启用 irqbalance，需要手动安装并启用
- memcg_test_3: 超时，复测后通过
- df01_sh: df01 85 TWARN: Failed to release device '/dev/vdc1'：测试脚本未能释放分区，卸载参数不合适，测试用例本身问题；mkfs 和 mkswap 均为此问题，下同
- mkfs01_sh: mkfs01 6 TWARN: Failed to release device '/dev/vdc1'
- mkfs01_ext2_sh: mkfs01 6 TWARN: Failed to release device '/dev/vdc1'
- mkfs01_ext3_sh: mkfs01 6 TWARN: Failed to release device '/dev/vdc1'
- mkfs01_ext4_sh: mkfs01 6 TWARN: Failed to release device '/dev/vdc1'
- mkfs01_xfs_sh: mkfs01 6 TWARN: Failed to release device '/dev/vdc1'
- mkfs01_btrfs_sh: mkfs01 6 TWARN: Failed to release device '/dev/vdc1'
- mkfs01_minix_sh: mkfs01 2 TWARN: Failed to release device '/dev/vdc1'
- mkfs01_msdos_sh: mkfs01 6 TWARN: Failed to release device '/dev/vdc1'
- mkfs01_vfat_sh: mkfs01 6 TWARN: Failed to release device '/dev/vdc1'
- mkfs01_ntfs_sh: mkfs01 6 TWARN: Failed to release device '/dev/vdc1'
- mkswap01_sh: mkswap01 11 TWARN: Failed to release device '/dev/vdc1'
- wqueue01: common.h:86: TBROK: add_key error: EKEYREVOKED：内核默认未开启 WATCH_QUEUE，下同
- wqueue02: common.h:86: TBROK: add_key error: EKEYREVOKED
- wqueue03: common.h:86: TBROK: add_key error: EKEYREVOKED
- wqueue04: common.h:86: TBROK: add_key error: EKEYREVOKED
- wqueue05: common.h:86: TBROK: add_key error: EKEYREVOKED
- wqueue06: common.h:86: TBROK: add_key error: EKEYREVOKED
- wqueue07: common.h:86: TBROK: add_key error: EKEYREVOKED
- wqueue08: common.h:86: TBROK: add_key error: EKEYREVOKED
- wqueue09: common.h:86: TBROK: add_key error: EKEYREVOKED

### 日志

附有此次 LTP 测试产生的 `output` 目录和 `results` 目录，位于 [log/old/6.1.19-default/](./log/old/6.1.19-default/)。

- `results/LTP_RUN_ON-2023_04_30-08h_15m_39s.log`：测试结果统计。
- `output/LTP_RUN_ON-tests.output.failed` 失败测试的名字（tag）及具体命令。
- `output/LTP_RUN_ON-tests.output.tconf`：（可能）需要调整配置的测试名（tag）及具体命令，包括且大部分为主动跳过的测试。
- `output/tests.output.gz`：所有测试的日志，因原文件过大，故使用 Gzip 压缩。
- `output/cpuctl_results_stress-*.txt`：从文件名上看，似乎为进行 CPU 相关测试时产生的输出，但是这几个文件都只有一行日期。

详见 [log](log/6.1.19-sv39/)

## 测试结论

测试共出现 31 项失败。

测试出现的部分问题在采取修正措施后复测可通过，复测无法通过的测试用例多为内核缺少对应配置，以及系统环境不支持，还有部分是测试用例本身存在问题，内核本身质量良好，未出现可靠性、稳定性问题。