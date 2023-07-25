# netpert 网络性能测试

## 概述

Netperf是一种网络性能测试工具，主要基于TCP或UDP的传输。etperf根据应用的不同，可以进行不同模式的网络性能测试，即批量数据传输（bulk data transfer）模式和请求/应答（request/reponse）模式。可以测量TCP和UDP传输的吞吐量、时延、CPU 占用率等性能参数。Netperf测试结果所反映的是一个系统能够以多快的速度向另一个系统发送数据，以及另一个系统能够以多快的速度接收数据。

## 测试环境

- 发行版版本：openEuler 23.03 RISC-V Preview V1
- 内核版本：6.1.19
- 虚拟机版本：QEMU 8.0.2

## 测试方法

见 [method.md](./method.md)

## 测试结果

### QEMU 测试结果

| 测试项目                         | 测试结果    |
|------------------------------|---------|
| TCP STREAM                   | 0.31    |
| TCP STREAM                   | 19.29   |
| TCP STREAM                   | 34.05   |
| TCP STREAM                   | 55.68   |
| TCP STREAM                   | 87.81   |
| TCP STREAM                   | 143.09  |
| TCP STREAM                   | 172.2   |
| TCP STREAM                   | 231.84  |
| TCP STREAM                   | 503.5   |
| TCP STREAM                   | 682.53  |
| TCP STREAM                   | 802.42  |
| TCP STREAM                   | 711.28  |
| TCP STREAM                   | 738.58  |
| UDP STREAM                   | 0.12    |
| UDP STREAM                   | 7.38    |
| UDP STREAM                   | 15.2    |
| UDP STREAM                   | 30.13   |
| UDP STREAM                   | 59.97   |
| UDP STREAM                   | 119     |
| UDP STREAM                   | 132.26  |
| UDP STREAM                   | 179.85  |
| UDP STREAM                   | 299.44  |
| UDP STREAM                   | 389.76  |
| UDP STREAM                   | 479.16  |
| UDP STREAM                   | 566.07  |
| TCP REQUEST/RESPONSE         | 2041.68 |
| TCP Connect/Request/Response | 726.03  |
| UDP REQUEST/RESPONSE         | 1890.8  |
