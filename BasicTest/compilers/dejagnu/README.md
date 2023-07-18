# dejagnu

DejaGnu 是一个用于测试其他程序的框架。

```
dejagnu
├── logs	#rv64 和 x86_64 测试日志
│   ├── riscv64
│   │   ├── full-log
│   │   │   ├── g++.log.zst
│   │   │   ├── g++.sum.zst
│   │   │   ├── gcc.log.zst
│   │   │   ├── gcc.sum.zst
│   │   │   ├── gfortran.log.zst
│   │   │   └── gfortran.sum.zst
│   │   ├── g++
│   │   │   ├── patchable_function_entry-decl.log
│   │   │   ├── patchable_function_entry-decl.sum
│   │   │   ├── patchable_function_entry-default.log
│   │   │   ├── patchable_function_entry-default.sum
│   │   │   ├── patchable_function_entry-definition.log
│   │   │   ├── patchable_function_entry-definition.sum
│   │   │   ├── pr99305.log
│   │   │   ├── pr99305.sum
│   │   │   ├── spec-barrier-1.log
│   │   │   └── spec-barrier-1.sum
│   │   ├── gcc
│   │   │   ├── get-edge-prob-non-init.log
│   │   │   ├── get-edge-prob-non-init.sum
│   │   │   ├── inline5.log
│   │   │   ├── inline5.sum
│   │   │   ├── patchable_function_entry-decl.log
│   │   │   ├── patchable_function_entry-decl.sum
│   │   │   ├── patchable_function_entry-default.log
│   │   │   ├── patchable_function_entry-default.sum
│   │   │   ├── patchable_function_entry-definition.log
│   │   │   ├── patchable_function_entry-definition.sum
│   │   │   ├── spec-barrier-1.log
│   │   │   └── spec-barrier-1.sum
│   │   └── gfortran
│   │       ├── ieee_6.log
│   │       ├── ieee_6.sum
│   │       ├── pr45636.log
│   │       ├── pr45636.sum
│   │       ├── pr95690.log
│   │       └── pr95690.sum
│   └── x86_64
│       ├── full-log
│       │   ├── g++.log.zst
│       │   ├── g++.sum.zst
│       │   ├── gcc.log.zst
│       │   ├── gcc.sum.zst
│       │   ├── gfortran.log.zst
│       │   └── gfortran.sum.zst
│       ├── g++
│       │   ├── patchable_function_entry-decl.log
│       │   ├── patchable_function_entry-decl.sum
│       │   ├── patchable_function_entry-default.log
│       │   ├── patchable_function_entry-default.sum
│       │   ├── patchable_function_entry-definition.log
│       │   ├── patchable_function_entry-definition.sum
│       │   ├── pr99305.log
│       │   ├── pr99305.sum
│       │   ├── spec-barrier-1.log
│       │   └── spec-barrier-1.sum
│       ├── gcc
│       │   ├── get-edge-prob-non-init.log
│       │   ├── get-edge-prob-non-init.sum
│       │   ├── inline5.log
│       │   ├── inline5.sum
│       │   ├── patchable_function_entry-decl.log
│       │   ├── patchable_function_entry-decl.sum
│       │   ├── patchable_function_entry-default.log
│       │   ├── patchable_function_entry-default.sum
│       │   ├── patchable_function_entry-definition.log
│       │   ├── patchable_function_entry-definition.sum
│       │   ├── spec-barrier-1.log
│       │   └── spec-barrier-1.sum
│       └── gfortran
│           ├── ieee_6.log
│           ├── ieee_6.sum
│           ├── pr45636.log
│           ├── pr45636.sum
│           ├── pr95690.log
│           └── pr95690.sum
├── method.md	#测试方法
├── README.md	#测试说明
├── result.md	#测试结果
└── src
    └── rerun-scripts	#失败项重测脚本
        ├── g++.sh
        ├── gcc.sh
        └── gfortran.sh
```