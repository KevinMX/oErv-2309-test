## 测试方法

- 从 [GitHub 仓库](https://github.com/kernelslacker/trinity) 获取 Trinity 源代码。以非 root 用户使用 `./configure && make -j4` 进行编译后，
- 使用 `./trinity` 运行测试。如需减少日志输出，节省硬盘空间，可添加 -q 或 -qq 参数：`./trinity -qq`
- 运行结束后进入 `tmp` 目录查看日志。其中，`trinity.log` 为主进程的日志，`trinity-child*.log` 为各子进程的日志。
