# LTP 测试

LTP 是由 SGI, OSDL 和 Bull 联合开发的项目，并由 IBM, Cisco, Fujitsu, SUSE, Red Hat, Oracle 和其他维护，其目的是向开源社区提供用于验证 Linux 可靠性、健壮性和稳定性的测试套件。

## 文件树

```
LTP
├── log
│   ├── 6.1.19-sv39 #开启 sv39 后进行的测试结果与日志
│   │   ├── failed.list
│   │   ├── ltp.log.gz
│   │   └── README.md
│   └── old
│       ├── 6.1.19-default  #未开启 sv39，使用默认内核进行的测试
│       │   ├── output
│       │   │   ├── cpuctl_results_stress-10.txt
│       │   │   ├── cpuctl_results_stress-678.txt
│       │   │   ├── cpuctl_results_stress-9.txt
│       │   │   ├── LTP_RUN_ON-tests.output.failed
│       │   │   ├── LTP_RUN_ON-tests.output.tconf
│       │   │   └── tests.output.7z
│       │   ├── README.md
│       │   └── results
│       │       └── LTP_RUN_ON-2023_04_30-08h_15m_39s.log
│       └── 6.1.19-newkconfig-rerun #未开启 sv39，使用修订版内核进行的测试
│           ├── output
│           │   ├── cpuctl_results_stress-10.txt
│           │   ├── cpuctl_results_stress-678.txt
│           │   ├── cpuctl_results_stress-9.txt
│           │   ├── LTP_RUN_ON-tests.output.failed
│           │   ├── LTP_RUN_ON-tests.output.tconf
│           │   └── tests.output.zst
│           ├── README.md
│           ├── res.csv
│           └── results
│               └── LTP_RUN_ON-2023_05_06-16h_33m_50s.log
├── method.md   #测试方法
├── README.md   #测试说明
└── result.md   #测试结果
``