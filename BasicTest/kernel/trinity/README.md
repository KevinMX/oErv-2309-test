# Trinity 测试

Trinity 是对内核 API 进行冒烟测试的套件。

## 环境信息

- 发行版版本：openEuler 23.03 RISC-V Preview V1
- 内核版本：6.1.19
- 虚拟机版本：QEMU 7.2.0
- 宿主机：Debian 11

## 其他信息

替换内核后，重新运行的结果请参考 [内核日志](./rerun/dmesg.log) 和 [Trinity 日志](./rerun/trinity.log.zst)。trinity 日志文件过大，采用 zstd 压缩。

> Note: 出现了同样的 CPU lockup 问题。

在 openEuler 23.03 x86_64 实机上执行了 trinity 测试。测试执行了约四天（92h），未出现内核锁死/崩溃等故障。

硬件信息：Intel Core i5-8259U, 16G RAM, 128G SATA SSD

软件信息：openEuler 23.03 x86_64, Linux 6.1.19-7.0.0.17.oe2303.x86_64, 采用官网镜像，最小安装。

日志请见 [log/x86_64](./log/x86_64/) 目录。由于文件较大，未上传 trinity 子线程日志，仅上传内核日志和 trinity 主线程日志，并采用 zstd 压缩，请解压后查看。

除了 trinity 主动触发的 OOM，以及 i915 提示 `Unexpected DP dual mode adaptor` 之外（与测试机未接显示器有关），无其他问题。

## 文件树

trinity
├── log #测试日志与结果
│   ├── kmesg.log
│   ├── rerun
│   │   ├── dmesg.log
│   │   ├── README.md
│   │   └── trinity.log.zst
│   ├── trinity.7z
│   └── x86_64
│       ├── dmesg.log.zst
│       └── trinity.log.zst
├── method.md   #测试方法
├── README.md   #测试说明
└── result.md   #测试结果