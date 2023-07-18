## 测试方法

执行：

```bash
git clone https://gitee.com/thesamename/STREAM.git
cd STREAM
sudo dnf install -y gcc gfortran
sed -i "s/CC =.*/CC = gcc/" Makefile
sed -i "s/FC =.*/FC = gfortran/" Makefile
make
./stream_c.exe
```