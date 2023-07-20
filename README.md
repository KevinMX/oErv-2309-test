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
