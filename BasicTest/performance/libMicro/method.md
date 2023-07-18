## 测试方法

执行：

```bash
wget https://codeload.github.com/redhat-performance/libMicro/zip/0.4.0-rh
unzip 0.4.0-rh
cd libMicro-0.4.0-rh
make CFLAGS=-static CC=${CROSS_COMPILE}gcc ARCH=${ARCH} -j$(nproc)
sh bench.sh
```