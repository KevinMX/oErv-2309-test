# netpert 测试

Netperf是一种网络性能测试工具，主要基于TCP或UDP的传输。etperf根据应用的不同，可以进行不同模式的网络性能测试，即批量数据传输（bulk data transfer）模式和请求/应答（request/reponse）模式。可以测量TCP和UDP传输的吞吐量、时延、CPU 占用率等性能参数。Netperf测试结果所反映的是一个系统能够以多快的速度向另一个系统发送数据，以及另一个系统能够以多快的速度接收数据。

## 文件树

```
netperf
├── log
│   └── res.log
├── method.md   #测试方法
├── README.md   #测试说明
└── result.md   #测试结果
```