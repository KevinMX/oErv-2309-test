## 测试方法

使用 Linux Test Project（简称 LTP）对内核进行测试。本次测试使用的 LTP 版本为 [20230516](https://github.com/linux-test-project/ltp/releases/tag/20230516)。

### 准备两个测试用虚拟盘

在宿主机：

```bash
qemu-img create -f qcow2 ext2g.qcow2 2G
qemu-img create -f qcow2 ext1g.qcow2 1G
```

同时，在 QEMU 命令行中增加以下参数：

```bash
  -drive file=ext2g.qcow2,format=qcow2,id=hd1 \
  -drive file=ext1g.qcow2,format=qcow2,id=hd2 \
  -device virtio-blk-device,drive=hd1 \
  -device virtio-blk-device,drive=hd2 \
```

### 测试内部环境准备

#### 安装测试所需的工具

```bash
dnf install -y gcc git make pkgconf autoconf automake bison flex m4 kernel-tools kernel-headers kernel-devel glibc-headers openssl-devel libacl-devel libaio-devel libcap-devel ethtool expect-devel xfsprogs-devel btrfs-progs quota nfs-utils libmnl-devel libtirpc-devel
```

#### 对新硬盘分区

在虚拟机，将其各分为一个区，格式化为 ext4：

```bash
fdisk /dev/vdb
mkfs.ext4 /dev/vdb1
fdisk /dev/vdc
mkfs.ext4 /dev/vdc1
```

#### 去除内存限制

删去 `/boot/extlinux/extlinux.conf` 中的 `mem=4096M`。

#### 重新启动

运行 `reboot` 重新启动虚拟机。

### 下载、编译、安装 LTP

```bash
wget https://github.com/linux-test-project/ltp/releases/download/20230516/ltp-full-20230516.tar.xz
tar -xvf ltp-full-20230516.tar.xz
cd ltp-full-20230516
make autotools
./configure --with-bash --with-expect --with-perl --with-python
make
make install
```

### 运行测试

为防止测试超时错误，增大超时限制的倍数。

```bash
export LTP_TIMEOUT_MUL=10
```

测试的临时文件目录默认是 `/tmp`，但 openEuler 已将其安装为 tmpfs，这会导致很多测试意外失败。因此专门建立一个目录，并在运行脚本参数中指明。

```bash
mkdir -p /ltp/tmp
```

运行：

```bash
cd /opt/ltp
./runltp -p -o tests.output -d /ltp/tmp -b /dev/vdc1 -B ext4 -z /dev/vdb1 -Z ext4
```
