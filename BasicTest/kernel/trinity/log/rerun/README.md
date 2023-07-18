# Trinity 测试

Trinity 是对内核 API 进行冒烟测试的套件。

## 环境信息

- 发行版版本：openEuler 23.03 RISC-V Preview V1
- 内核版本：6.1.19-0.0.0.0.oe2303.riscv64
- 虚拟机版本：QEMU 8.0.0
- 宿主机：Arch Linux on WSL 2, Windows 10 IoT Enterprise LTSC

## 测试步骤

- 替换修订版内核。

使用的内核是经过修复的 [kernel-6.1.19-0.0.0.0.oe2303.riscv64.rpm](http://obs-backend.tarsier-infra.com:82/home:/laokz:/branches:/openEuler:/23.03/23.02/riscv64/kernel-6.1.19-0.0.0.0.oe2303.riscv64.rpm)。

1. 启动原虚拟机，在虚拟机内使用 `rpm -i` 解压新内核，将 `/boot/vmlinuz-6.1.19-0.0.0.0.oe2303.riscv64` 拷贝到宿主机。

2. 关机，将宿主机上的 `vmlinuz-6.1.19-0.0.0.0.oe2303.riscv64` 重命名为 `vmlinuz.gz`

3. 使用 `gunzip` 解压缩 `vmlinuz.gz`。

4. 添加 `qemu` 启动参数 `-kernel=vmlinuz` ，添加 `-append "root=/dev/vda2"`，移除 `-bios`，然后启动虚拟机。

- 从 [GitHub 仓库](https://github.com/kernelslacker/trinity) 获取 Trinity 源代码。以非 root 用户使用 `./configure && make -j4` 进行编译。

- 使用 `./trinity -v | tee log` 运行测试。

## 测试结果

替换内核后，重新运行的结果请参考 [内核日志](./dmesg.log) 和 [Trinity 日志](./trinity.log.zst)。trinity 日志文件过大，采用 zstd 压缩。与替换内核前相同，出现了 `CPU lockup` 问题。

> trinity: Detected kernel tainting. Last seed was 2466001601

> watchdog: BUG: soft lockup - CPU#0 stuck for 62671s! [trinity-c4:10628]
