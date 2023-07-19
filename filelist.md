# openEuler 23.03 RISC-V 测试报告审查表

打勾以表示通过 sig-QA 审查，并在后面注明通过时间。

## 基础测试

```
├── compilers
│   ├── AnghaBench
│   │   ├── log
│   │   │   ├── AnghaBench.log.gz
│   │   │   ├── arch.md
│   │   │   ├── compilation_log.tar.gz
│   │   │   └── testcase_problem.md
│   │   ├── method.md
│   │   ├── README.md
│   │   ├── result.md
│   │   └── src
│   │       └── compile.sh
│   ├── csmith
│   │   ├── log
│   │   │   └── csmith.log
│   │   ├── method.md
│   │   ├── README.md
│   │   ├── result.md
│   │   └── src
│   │       ├── csrc.mk
│   │       ├── epoch.sh
│   │       ├── list.mk
│   │       └── makefile
│   ├── dejagnu
│   │   ├── logs
│   │   │   ├── riscv64
│   │   │   │   ├── full-log
│   │   │   │   │   ├── g++.log.zst
│   │   │   │   │   ├── g++.sum.zst
│   │   │   │   │   ├── gcc.log.zst
│   │   │   │   │   ├── gcc.sum.zst
│   │   │   │   │   ├── gfortran.log.zst
│   │   │   │   │   └── gfortran.sum.zst
│   │   │   │   ├── g++
│   │   │   │   │   ├── patchable_function_entry-decl.log
│   │   │   │   │   ├── patchable_function_entry-decl.sum
│   │   │   │   │   ├── patchable_function_entry-default.log
│   │   │   │   │   ├── patchable_function_entry-default.sum
│   │   │   │   │   ├── patchable_function_entry-definition.log
│   │   │   │   │   ├── patchable_function_entry-definition.sum
│   │   │   │   │   ├── pr99305.log
│   │   │   │   │   ├── pr99305.sum
│   │   │   │   │   ├── spec-barrier-1.log
│   │   │   │   │   └── spec-barrier-1.sum
│   │   │   │   ├── gcc
│   │   │   │   │   ├── get-edge-prob-non-init.log
│   │   │   │   │   ├── get-edge-prob-non-init.sum
│   │   │   │   │   ├── inline5.log
│   │   │   │   │   ├── inline5.sum
│   │   │   │   │   ├── patchable_function_entry-decl.log
│   │   │   │   │   ├── patchable_function_entry-decl.sum
│   │   │   │   │   ├── patchable_function_entry-default.log
│   │   │   │   │   ├── patchable_function_entry-default.sum
│   │   │   │   │   ├── patchable_function_entry-definition.log
│   │   │   │   │   ├── patchable_function_entry-definition.sum
│   │   │   │   │   ├── spec-barrier-1.log
│   │   │   │   │   └── spec-barrier-1.sum
│   │   │   │   └── gfortran
│   │   │   │       ├── ieee_6.log
│   │   │   │       ├── ieee_6.sum
│   │   │   │       ├── pr45636.log
│   │   │   │       ├── pr45636.sum
│   │   │   │       ├── pr95690.log
│   │   │   │       └── pr95690.sum
│   │   │   └── x86_64
│   │   │       ├── full-log
│   │   │       │   ├── g++.log.zst
│   │   │       │   ├── g++.sum.zst
│   │   │       │   ├── gcc.log.zst
│   │   │       │   ├── gcc.sum.zst
│   │   │       │   ├── gfortran.log.zst
│   │   │       │   └── gfortran.sum.zst
│   │   │       ├── g++
│   │   │       │   ├── patchable_function_entry-decl.log
│   │   │       │   ├── patchable_function_entry-decl.sum
│   │   │       │   ├── patchable_function_entry-default.log
│   │   │       │   ├── patchable_function_entry-default.sum
│   │   │       │   ├── patchable_function_entry-definition.log
│   │   │       │   ├── patchable_function_entry-definition.sum
│   │   │       │   ├── pr99305.log
│   │   │       │   ├── pr99305.sum
│   │   │       │   ├── spec-barrier-1.log
│   │   │       │   └── spec-barrier-1.sum
│   │   │       ├── gcc
│   │   │       │   ├── get-edge-prob-non-init.log
│   │   │       │   ├── get-edge-prob-non-init.sum
│   │   │       │   ├── inline5.log
│   │   │       │   ├── inline5.sum
│   │   │       │   ├── patchable_function_entry-decl.log
│   │   │       │   ├── patchable_function_entry-decl.sum
│   │   │       │   ├── patchable_function_entry-default.log
│   │   │       │   ├── patchable_function_entry-default.sum
│   │   │       │   ├── patchable_function_entry-definition.log
│   │   │       │   ├── patchable_function_entry-definition.sum
│   │   │       │   ├── spec-barrier-1.log
│   │   │       │   └── spec-barrier-1.sum
│   │   │       └── gfortran
│   │   │           ├── ieee_6.log
│   │   │           ├── ieee_6.sum
│   │   │           ├── pr45636.log
│   │   │           ├── pr45636.sum
│   │   │           ├── pr95690.log
│   │   │           └── pr95690.sum
│   │   ├── method.md
│   │   ├── README.md
│   │   ├── result.md
│   │   └── src
│   │       └── rerun-scripts
│   │           ├── g++.sh
│   │           ├── gcc.sh
│   │           └── gfortran.sh
│   ├── jotai
│   │   ├── log
│   │   │   ├── anghaLeaves.fail
│   │   │   ├── anghaMath.fail
│   │   │   ├── old
│   │   │   │   ├── jotai.log
│   │   │   │   └── jotai.md
│   │   │   └── test.log.gz
│   │   ├── method.md
│   │   ├── README.md
│   │   ├── result.md
│   │   └── src
│   │       ├── Makefile
│   │       └── singletest.lua
│   └── yarpgen
│       ├── method.md
│       ├── README.md
│       ├── result.md
│       └── src
│           └── auto_test.sh
├── function
│   └── LTP
│       ├── log
│       │   ├── 6.1.19-sv39
│       │   │   ├── failed.list
│       │   │   ├── ltp.log.gz
│       │   │   └── README.md
│       │   └── old
│       │       ├── 6.1.19-default
│       │       │   ├── output
│       │       │   │   ├── cpuctl_results_stress-10.txt
│       │       │   │   ├── cpuctl_results_stress-678.txt
│       │       │   │   ├── cpuctl_results_stress-9.txt
│       │       │   │   ├── LTP_RUN_ON-tests.output.failed
│       │       │   │   ├── LTP_RUN_ON-tests.output.tconf
│       │       │   │   └── tests.output.7z
│       │       │   ├── README.md
│       │       │   └── results
│       │       │       └── LTP_RUN_ON-2023_04_30-08h_15m_39s.log
│       │       └── 6.1.19-newkconfig-rerun
│       │           ├── output
│       │           │   ├── cpuctl_results_stress-10.txt
│       │           │   ├── cpuctl_results_stress-678.txt
│       │           │   ├── cpuctl_results_stress-9.txt
│       │           │   ├── LTP_RUN_ON-tests.output.failed
│       │           │   ├── LTP_RUN_ON-tests.output.tconf
│       │           │   └── tests.output.zst
│       │           ├── README.md
│       │           ├── res.csv
│       │           └── results
│       │               └── LTP_RUN_ON-2023_05_06-16h_33m_50s.log
│       ├── method.md
│       ├── README.md
│       └── result.md
├── kernel
│   └── trinity
│       ├── log
│       │   ├── kmesg.log
│       │   ├── rerun
│       │   │   ├── dmesg.log
│       │   │   ├── README.md
│       │   │   └── trinity.log.zst
│       │   ├── trinity.7z
│       │   └── x86_64
│       │       ├── dmesg.log.zst
│       │       └── trinity.log.zst
│       ├── method.md
│       ├── README.md
│       └── result.md
├── long_stress
│   └── LTPstress
│       ├── log
│       │   └── ltpstress.tar.zst
│       ├── method.md
│       ├── README.md
│       ├── result.md
│       └── src
│           └── run_ltpstress.sh
└── performance
    ├── fio
    │   ├── log
    │   │   ├── LicheeRVD1.log
    │   │   ├── NezhaD1.log
    │   │   ├── QEMU.log
    │   │   ├── Unmatched.log
    │   │   ├── VisionFive1.log
    │   │   └── VisionFive2.log
    │   ├── method.md
    │   ├── README.md
    │   └── result.md
    ├── libMicro
    │   ├── log
    │   │   ├── LicheeRVD1.log
    │   │   ├── NezhaD1.log
    │   │   ├── QEMU.log
    │   │   ├── Unmatched.log
    │   │   ├── VisionFive1.log
    │   │   └── VisionFive2.log
    │   ├── method.md
    │   ├── README.md
    │   └── result.md
    ├── lmbench
    │   ├── log
    │   │   ├── images
    │   │   │   ├── percent-diff.png
    │   │   │   └── summary-diff.png
    │   │   ├── LicheeRVD1
    │   │   │   ├── LicheeRVD1.log
    │   │   │   ├── openeuler-riscv64.0
    │   │   │   ├── percent.errs
    │   │   │   ├── percent.out
    │   │   │   ├── summary.errs
    │   │   │   └── summary.out
    │   │   ├── NezhaD1
    │   │   │   ├── NezhaD1.log
    │   │   │   ├── openeuler-riscv64.0
    │   │   │   ├── percent.errs
    │   │   │   ├── percent.out
    │   │   │   ├── summary.errs
    │   │   │   └── summary.out
    │   │   ├── QEMU
    │   │   │   ├── openeuler-riscv64.0
    │   │   │   ├── percent.errs
    │   │   │   ├── percent.out
    │   │   │   ├── QEMU.log
    │   │   │   ├── QEMU-dmesg.log
    │   │   │   ├── summary.errs
    │   │   │   └── summary.out
    │   │   ├── Unmatched
    │   │   │   ├── openeuler-riscv64.0
    │   │   │   ├── percent.errs
    │   │   │   ├── percent.out
    │   │   │   ├── summary.errs
    │   │   │   ├── summary.out
    │   │   │   ├── Unmatched.log
    │   │   │   └── Unmatched-dmesg.log
    │   │   ├── VisionFive1
    │   │   │   ├── openeuler-riscv64.0
    │   │   │   ├── percent.errs
    │   │   │   ├── percent.out
    │   │   │   ├── summary.errs
    │   │   │   ├── summary.out
    │   │   │   ├── VisionFive1.log
    │   │   │   └── VisionFive1-dmesg.log
    │   │   ├── VisionFive2
    │   │   │   ├── openeuler-riscv64.0
    │   │   │   ├── percent.errs
    │   │   │   ├── percent.out
    │   │   │   ├── summary.errs
    │   │   │   ├── summary.out
    │   │   │   └── VisionFive2.log
    │   │   └── x86_64
    │   │       ├── Makefile
    │   │       ├── percent.errs
    │   │       ├── percent.out
    │   │       ├── summary.errs
    │   │       ├── summary.out
    │   │       └── x86_64-linux-gnu
    │   │           └── localhost.localdomain.0
    │   ├── method.md
    │   ├── README.md
    │   └── result.md
    ├── netperf
    │   ├── log
    │   │   └── res.log
    │   ├── method.md
    │   ├── README.md
    │   └── result.md
    ├── stream
    │   ├── log
    │   │   ├── LicheeRVD1.log
    │   │   ├── NezhaD1.log
    │   │   ├── QEMU.log
    │   │   ├── Unmatched.log
    │   │   ├── VisionFive1.log
    │   │   └── VisionFive2.log
    │   ├── method.md
    │   ├── README.md
    │   └── result.md
    └── unixbench
        ├── log
        │   ├── LecheeRVD1.log
        │   ├── NezhaD1.log
        │   ├── QEMU.log
        │   ├── Unmatched.log
        │   ├── VisionFive1.log
        │   └── VisionFive2.log
        ├── method.md
        ├── README.md
        └── result.md
```