# 测试方法

> 与上游不同之处：直接从软件源安装 dejagnu 而非编译安装。

1. 安装 dejagnu 和 GCC

```bash
sudo dnf install -y dejagnu gcc gcc-*
```

2. 获取 `gcc` 源码及其自带的测试套

```bash
git clone --depth=1 https://gitee.com/openeuler/gcc
cd gcc/gcc/testsuite
```

3. 分别运行 gcc, g++, gfortran 的测试套

```bash
runtest --tool gcc
runtest --tool g++
runtest --tool gfortran
```

4. 查看测试结果

测试结束后，会在当前目录下生成 `.log` 日志文件和 `.sum` 统计信息，可进行查看。

## Extra. 针对已知会出现报错的部分测试用例进行单独测试

可使用 [rerun-scripts](./src/rerun-scripts/) 下提供的脚本。

```bash
cd gcc/gcc/testsuite
bash gcc.sh; bash g++.sh; bash gfortran.sh
```

运行完成后，在 `~/log` 下查看对应日志。