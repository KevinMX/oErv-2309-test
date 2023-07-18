# 测试方法

执行：

```bash
git clone https://github.com/kdlucas/byte-unixbench
cd byte-unixbench/UnixBench
make -j$(nproc)
./Run -c $(nproc)
```