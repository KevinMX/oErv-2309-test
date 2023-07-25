# AnghaBench 测试方案

## 环境

- 发行版版本：openEuler 23.03 RISC-V Preview V1
- 虚拟机版本：QEMU 7.2.0

## 执行测试

从 [此](https://github.com/brenocfg/AnghaBench/) 获得 AnghaBench 项目代码并使用 [该脚本](./src/compile.sh) 运行测试

```bash
git clone https://github.com/brenocfg/AnghaBench/
cp ./compile.sh ./AnghaBench/compile.sh
cd ./AnghaBench/
bash ./compile.sh | tee ../res.log
```