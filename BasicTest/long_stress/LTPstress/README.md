# LTP Stress 长稳测试

Linux Test Project / LTP 中的 stress 组件可用于对内核进行压稳测试。

## 环境信息

- 发行版版本：openEuler 23.03 RISC-V Preview V1
- 内核版本：6.1.19
- 虚拟机版本：QEMU 8.0.2
- 宿主机：Arch Linux on WSL 2
- 软件版本：LTP 20230516 release ([GitHub](https://github.com/linux-test-project/ltp/releases/tag/20230516))

## 与上游测试方法不同之处

对脚本做了一定修改，方便一键执行。目前脚本默认压测 24 小时，如需修改，请将脚本中的 `sh ltpstress.sh -n -m 512 -t 24` 的 24 修改为其他数值。

## 参考文档

https://gitee.com/hanson_fang/ltpstress-for-openeuler

本目录下提供的 `run_ltpstress.sh` 脚本是在此仓库提供的脚本基础上修改而成。

## 文件树

```
LTPstress
├── log #日志
│   └── ltpstress.tar.zst
├── method.md   #测试方法
├── README.md   #测试说明
├── result.md   #测试结果
└── src
    └── run_ltpstress.sh    #自动测试脚本
```