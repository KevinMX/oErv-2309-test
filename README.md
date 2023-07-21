# openEuler 23.03 RISC-V 测试报告交付物清单

## 编译器测试

- [AnghaBench](/BasicTest/compilers/AnghaBench/)
- [csmith](/BasicTest/compilers/csmith/)
- [dejagnu](/BasicTest/compilers/dejagnu/)
- [jotai](/BasicTest/compilers/jotai/)
- [yarpgen](/BasicTest/compilers/yarpgen/)
    
## 功能测试

- [mugen BaseOS](https://gitee.com/yunxiangluo/openeuler-riscv-2303-test/tree/master/23.09/mugen)
- [LTP](/BasicTest/function/LTP/)

## 内核测试

- [trinity](/BasicTest/kernel/trinity/)

## 性能测试

- [fio](/BasicTest/performance/fio/)
- [libMicro](/BasicTest/performance/libMicro/)
- [lmbench](/BasicTest/performance/lmbench/)
- [netperf](/BasicTest/performance/netperf/)
- [stream](/BasicTest/performance/stream)
- [unixbench](/BasicTest/performance/unixbench/)

## 长稳测试

- [LTP Stress](/BasicTest/long_stress/LTPstress/)

## QEMU 兼容性测试

- [QEMU 8.0 +](/docs/InstallationBook/QEMU/)

## 文档测试

- 对文档准确性进行验证

## 包括在 CI 门禁中的测试

- 系统集成
- 软件包管理

## 已取消的测试

- 安全测试
    - oss-fuzz
    - CVE 漏洞扫描
    - 安全编译选项
    - 敏感信息扫描
    - 交付件病毒扫描
- 北向兼容性
- 南向兼容性
    - 硬件开发板

## 五轮测试策略

### Round 1

- 功能测试
  - [mugen BaseOS](https://gitee.com/yunxiangluo/openeuler-riscv-2303-test/tree/master/23.09/mugen)
  - [LTP](/BasicTest/function/LTP/)
  - 保证 BaseOS 合入的基础上提供新特性验证
- 编译器测试
  - [AnghaBench](/BasicTest/compilers/AnghaBench/)
  - [csmith](/BasicTest/compilers/csmith/)
  - [dejagnu](/BasicTest/compilers/dejagnu/)
  - [jotai](/BasicTest/compilers/jotai/)
  - [yarpgen](/BasicTest/compilers/yarpgen/)
- 内核测试
  - [trinity](/BasicTest/kernel/trinity/)
- 性能测试
  - [fio](/BasicTest/performance/fio/)
  - [libMicro](/BasicTest/performance/libMicro/)
  - [lmbench](/BasicTest/performance/lmbench/)
  - [netperf](/BasicTest/performance/netperf/)
  - [stream](/BasicTest/performance/stream)
  - [unixbench](/BasicTest/performance/unixbench/)

### Round 2

- 功能测试
  - [mugen BaseOS](https://gitee.com/yunxiangluo/openeuler-riscv-2303-test/tree/master/23.09/mugen)
  - 保证 BaseOS 合入的基础上提供新特性验证
- 长稳测试
  - [LTP Stress](/BasicTest/long_stress/LTPstress/)（7*24）

### Round 3

- 功能测试
  - [mugen BaseOS](https://gitee.com/yunxiangluo/openeuler-riscv-2303-test/tree/master/23.09/mugen)
  - 保证 BaseOS 合入的基础上提供新特性验证
- 性能测试
  - [fio](/BasicTest/performance/fio/)
  - [libMicro](/BasicTest/performance/libMicro/)
  - [lmbench](/BasicTest/performance/lmbench/)
  - [netperf](/BasicTest/performance/netperf/)
  - [stream](/BasicTest/performance/stream)
  - [unixbench](/BasicTest/performance/unixbench/)
- 长稳测试
  - [LTP Stress](/BasicTest/long_stress/LTPstress/)
- 文档测试
  - 对已提供的安装文档和部分操作文档进行验证
- 问题单回归

### Round 4

- 功能测试
  - [mugen BaseOS](https://gitee.com/yunxiangluo/openeuler-riscv-2303-test/tree/master/23.09/mugen)
  - 保证 BaseOS 合入的基础上提供新特性验证
- 问题单回归
- 长稳测试
  - [LTP Stress](/BasicTest/long_stress/LTPstress/)
- 性能测试
  - [fio](/BasicTest/performance/fio/)
  - [libMicro](/BasicTest/performance/libMicro/)
  - [lmbench](/BasicTest/performance/lmbench/)
  - [netperf](/BasicTest/performance/netperf/)
  - [stream](/BasicTest/performance/stream)
  - [unixbench](/BasicTest/performance/unixbench/)
- 文档测试
  - 对已提供的安装文档和部分操作文档进行验证

### Round 5

- 功能测试
  - [mugen BaseOS](https://gitee.com/yunxiangluo/openeuler-riscv-2303-test/tree/master/23.09/mugen)
  - 保证 BaseOS 合入的基础上提供新特性验证
- 问题单全量回归
- 文档测试
  - 对已提供的安装文档和部分操作文档进行验证

## 入口标准

- 上个阶段无阻塞问题遗留。
- 转测版本的冒烟无阻塞性问题。

## 出口标准

- 策略规划的测试活动涉及测试用例 100% 执行完毕。
- 发布特性/新需求/性能基线等满足版本规划目标。
- 版本无阻塞问题遗留，其它严重问题要有相应规避措施或说明。