## 6.1.19 内核默认配置

- 测试用例总数：2379
- 跳过的：308
- 失败的：32

### 失败结果评估

将超时的失败的用例进行重新测试，整理测试日志，得到如下结果。

- leapsec01.c:84: TBROK: adjtimex status 8208 not set：
- clock_settime03: 超时
- getxattr04: tst_test.c:1107: TBROK: mount(/dev/vdc1, mntpoint, xfs, 0, (nil)) failed: ENODEV (19)
- fanotify10: TCONF: fanotify is not configured in this kernel
- keyctl03: keyctl03.c:31: TBROK: Failed to add key
- setfsuid02_16: setfsuid02.c:26: TBROK: uid -1 of invalid_uid is too large for testing 16-bit version of setfsuid()
- perf_event_open01: perf_event_open01    1  TFAIL  :  perf_event_open01.c:156: perf_event_open PERF_COUNT_HW_INSTRUCTIONS failed unexpectedly: TEST_ERRNO=EINVAL(22): Invalid argument
- vma05: vma05 1 TFAIL: [vdso] bug not patched
- irqbalance01: irqbalance01.c:287: TFAIL: Heuristic: Detected 0 irq-cpu pairs have been dissallowed
- memcg_test_3: 超时，复测后通过
- df01_sh: df01 85 TWARN: Failed to release device '/dev/vdc1'
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
- cve-2016-7042: cve-2016-7042.c:35: TBROK: Failed to add key
- wqueue01: common.h:86: TBROK: add_key error: EKEYREVOKED
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