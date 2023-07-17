# openEuler 23.03 RISC-V 测试报告审查表

打勾以表示通过 sig-QA 审查，并在后面注明通过时间。

## 基础测试

── 编译器测试
│   ├── AnghaBench
│   │   ├── AnghaBench.log.gz
│   │   ├── arch.md
│   │   ├── compilation_log.tar.gz
│   │   ├── compile.sh
│   │   ├── README.md
│   │   └── testcase_problem.md
│   ├── csmith
│   │   ├── csmith.log
│   │   ├── csrc.mk
│   │   ├── epoch.sh
│   │   ├── list.mk
│   │   ├── makefile
│   │   └── README.md
│   ├── dejagnu
│   │   ├── README.md
│   │   ├── rerun-scripts
│   │   │   ├── gcc.sh
│   │   │   ├── gfortran.sh
│   │   │   └── g++.sh
│   │   ├── riscv64
│   │   │   ├── full-log
│   │   │   │   ├── gcc.log.zst
│   │   │   │   ├── gcc.sum.zst
│   │   │   │   ├── gfortran.log.zst
│   │   │   │   ├── gfortran.sum.zst
│   │   │   │   ├── g++.log.zst
│   │   │   │   └── g++.sum.zst
│   │   │   ├── g++
│   │   │   │   ├── patchable_function_entry-decl.log
│   │   │   │   ├── patchable_function_entry-decl.sum
│   │   │   │   ├── patchable_function_entry-default.log
│   │   │   │   ├── patchable_function_entry-default.sum
│   │   │   │   ├── patchable_function_entry-definition.log
│   │   │   │   ├── patchable_function_entry-definition.sum
│   │   │   │   ├── pr99305.log
│   │   │   │   ├── pr99305.sum
│   │   │   │   ├── spec-barrier-1.log
│   │   │   │   └── spec-barrier-1.sum
│   │   │   ├── gcc
│   │   │   │   ├── get-edge-prob-non-init.log
│   │   │   │   ├── get-edge-prob-non-init.sum
│   │   │   │   ├── inline5.log
│   │   │   │   ├── inline5.sum
│   │   │   │   ├── patchable_function_entry-decl.log
│   │   │   │   ├── patchable_function_entry-decl.sum
│   │   │   │   ├── patchable_function_entry-default.log
│   │   │   │   ├── patchable_function_entry-default.sum
│   │   │   │   ├── patchable_function_entry-definition.log
│   │   │   │   ├── patchable_function_entry-definition.sum
│   │   │   │   ├── spec-barrier-1.log
│   │   │   │   └── spec-barrier-1.sum
│   │   │   └── gfortran
│   │   │       ├── ieee_6.log
│   │   │       ├── ieee_6.sum
│   │   │       ├── pr45636.log
│   │   │       ├── pr45636.sum
│   │   │       ├── pr95690.log
│   │   │       └── pr95690.sum
│   │   └── x86_64
│   │       ├── full-log
│   │       │   ├── gcc.log.zst
│   │       │   ├── gcc.sum.zst
│   │       │   ├── gfortran.log.zst
│   │       │   ├── gfortran.sum.zst
│   │       │   ├── g++.log.zst
│   │       │   └── g++.sum.zst
│   │       ├── g++
│   │       │   ├── patchable_function_entry-decl.log
│   │       │   ├── patchable_function_entry-decl.sum
│   │       │   ├── patchable_function_entry-default.log
│   │       │   ├── patchable_function_entry-default.sum
│   │       │   ├── patchable_function_entry-definition.log
│   │       │   ├── patchable_function_entry-definition.sum
│   │       │   ├── pr99305.log
│   │       │   ├── pr99305.sum
│   │       │   ├── spec-barrier-1.log
│   │       │   └── spec-barrier-1.sum
│   │       ├── gcc
│   │       │   ├── get-edge-prob-non-init.log
│   │       │   ├── get-edge-prob-non-init.sum
│   │       │   ├── inline5.log
│   │       │   ├── inline5.sum
│   │       │   ├── patchable_function_entry-decl.log
│   │       │   ├── patchable_function_entry-decl.sum
│   │       │   ├── patchable_function_entry-default.log
│   │       │   ├── patchable_function_entry-default.sum
│   │       │   ├── patchable_function_entry-definition.log
│   │       │   ├── patchable_function_entry-definition.sum
│   │       │   ├── spec-barrier-1.log
│   │       │   └── spec-barrier-1.sum
│   │       └── gfortran
│   │           ├── ieee_6.log
│   │           ├── ieee_6.sum
│   │           ├── pr45636.log
│   │           ├── pr45636.sum
│   │           ├── pr95690.log
│   │           └── pr95690.sum
│   ├── jotai
│   │   ├── analysis.md
│   │   ├── anghaLeaves.fail
│   │   ├── anghaMath.fail
│   │   ├── Makefile
│   │   ├── old
│   │   │   ├── jotai.log
│   │   │   └── jotai.md
│   │   ├── README.md
│   │   ├── singletest.lua
│   │   └── test.log.gz
│   └── yarpgen
│       ├── auto_test.sh
│       └── README.md
├── 长稳测试
│   └── LTPstress
│       ├── ltpstress
│       ├── ltpstress.tar.zst
│       ├── README.md
│       └── run_ltpstress.sh
├── 基础性能测试
│   ├── fio
│   │   ├── LicheeRVD1.log
│   │   ├── NezhaD1.log
│   │   ├── QEMU.log
│   │   ├── README.md
│   │   ├── Unmatched.log
│   │   ├── VisionFive1.log
│   │   └── VisionFive2.log
│   ├── libMicro
│   │   ├── LicheeRVD1.log
│   │   ├── NezhaD1.log
│   │   ├── QEMU.log
│   │   ├── README.md
│   │   ├── Unmatched.log
│   │   ├── VisionFive1.log
│   │   └── VisionFive2.log
│   ├── lmbench
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
│   │   │   ├── QEMU-dmesg.log
│   │   │   ├── QEMU.log
│   │   │   ├── summary.errs
│   │   │   └── summary.out
│   │   ├── README.md
│   │   ├── Unmatched
│   │   │   ├── openeuler-riscv64.0
│   │   │   ├── percent.errs
│   │   │   ├── percent.out
│   │   │   ├── summary.errs
│   │   │   ├── summary.out
│   │   │   ├── Unmatched-dmesg.log
│   │   │   └── Unmatched.log
│   │   ├── VisionFive1
│   │   │   ├── openeuler-riscv64.0
│   │   │   ├── percent.errs
│   │   │   ├── percent.out
│   │   │   ├── summary.errs
│   │   │   ├── summary.out
│   │   │   ├── VisionFive1-dmesg.log
│   │   │   └── VisionFive1.log
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
│   ├── netperf
│   │   ├── README.md
│   │   └── res.log
│   ├── stream
│   │   ├── LicheeRVD1.log
│   │   ├── NezhaD1.log
│   │   ├── QEMU.log
│   │   ├── README.md
│   │   ├── Unmatched.log
│   │   ├── VisionFive1.log
│   │   └── VisionFive2.log
│   └── unixbench
│       ├── LecheeRVD1.log
│       ├── NezhaD1.log
│       ├── QEMU.log
│       ├── README.md
│       ├── Unmatched.log
│       ├── VisionFive1.log
│       └── VisionFive2.log
└── 内核测试
    ├── LTP
    │   ├── output
    │   │   ├── cpuctl_results_stress-10.txt
    │   │   ├── cpuctl_results_stress-678.txt
    │   │   ├── cpuctl_results_stress-9.txt
    │   │   ├── LTP_RUN_ON-tests.output.failed
    │   │   ├── LTP_RUN_ON-tests.output.tconf
    │   │   └── tests.output.7z
    │   ├── README.md
    │   ├── rererun
    │   │   ├── failed.list
    │   │   ├── ltp.log.gz
    │   │   └── README.md
    │   ├── rerun
    │   │   ├── output
    │   │   │   ├── cpuctl_results_stress-10.txt
    │   │   │   ├── cpuctl_results_stress-678.txt
    │   │   │   ├── cpuctl_results_stress-9.txt
    │   │   │   ├── LTP_RUN_ON-tests.output.failed
    │   │   │   ├── LTP_RUN_ON-tests.output.tconf
    │   │   │   └── tests.output.zst
    │   │   ├── README.md
    │   │   ├── res.csv
    │   │   └── results
    │   │       └── LTP_RUN_ON-2023_05_06-16h_33m_50s.log
    │   └── results
    │       └── LTP_RUN_ON-2023_04_30-08h_15m_39s.log
    └── trinity
        ├── kmesg.log
        ├── README.md
        ├── rerun
        │   ├── dmesg.log
        │   ├── README.md
        │   └── trinity.log.zst
        ├── trinity.7z
        └── x86_64
            ├── dmesg.log.zst
            └── trinity.log.zst