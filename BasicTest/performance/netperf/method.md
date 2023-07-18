# 测试方法

## 连接两台 Qemu 测试机

参见 [适用于 Qemu 多节点的 VDE 网络配置指南](https://github.com/ArielHeleneto/Work-PLCT/blob/master/openMPI/VDE-network.md)，并确定两台 Qemu 测试机的 IP 地址。

### 设置 VDE 网络

首先设置 VDE 网络。

缺少相关包请安装 `VDE2`。

```bash
#!/bin/sh

vdeSocket=/tmp/vde.ctl
mgmtSocket=/tmp/mgmt

rm -rf $vdeSocket
rm -rf $mgmtSocket

# Check for vde tools

if ! [ -f /usr/bin/vde_switch ]
then
	echo "VDE tools not found."
	exit 1
fi

vde_switch -d -s $vdeSocket -M $mgmtSocket
slirpvde -d -s $vdeSocket -dhcp

echo "VDE socket is $vdeSocket, management socket is $mgmtSocket"
```

### Qemu 虚拟机相关设置

使用下列指令将 Qemu 虚拟机连接到 VDE 网络。在网络中 MAC 地址必须唯一，否则会分配相同地址导致错误。

```bash
macadd=$(echo $RANDOM|md5sum|sed 's/../&:/g'|cut -c 1-17)
-device virtio-net-device,netdev=innet,mac="$macadd" -netdev vde,id=innet,sock=/tmp/vde.ctl
```

## 准备环境

从软件源安装 `netperf`。

```bash
dnf install netperf -y
```

由下列命令确定包版本。

```bash
dnf info netperf
```

获得版本信息。

```text
Last metadata expiration check: 22:41:57 ago on Thu 04 May 2023 12:03:47 AM CST.
Installed Packages
Name         : netperf
Version      : 2.7.0
Release      : 5.oe2303
Architecture : riscv64
Size         : 550 k
Source       : netperf-2.7.0-5.oe2303.src.rpm
Repository   : @System
From repo    : mainline
Summary      : A Performance benchmark testing tool fro TCP/UDP
URL          : http://github.com/HewlettPackard/netperf
License      : MIT
Description  : netperf is a collection of  many different network performance
             : benchmarking tools
```

## 准备服务器

在服务器中运行下列指令启动服务器。

```bash
netserver
```

## 启动测试

将下列脚本保存到 `1.sh`

```bash
#!/bin/bash
host_ip=$1
for i in 1 64 128 256 512 1024 1500 2048 4096 9000 16384 32768 65536;do
./netperf -t TCP_STREAM -H $host_ip -l 60 -- -m $i
done
for i in 1 64 128 256 512 1024 1500 2048 4096 9000 16384 32768;do
./netperf -t UDP_STREAM -H $host_ip -l 60 -- -m $i -R 1
done
./netperf -t TCP_RR -H $host_ip
./netperf -t TCP_CRR -H $host_ip
./netperf -t UDP_RR -H $host_ip
```

并运行之。

```bash
bash 1.sh {Server-IP}
```

替换 `{Server-IP}` 为服务器 IP。从标准输出中获得测试结果。
