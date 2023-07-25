# fio 测试报告

## 概述

`fio` 是测试 IOPS 的工具，用来对磁盘进行压力测试和验证。磁盘 IO 是检查磁盘性能的重要指标，可以按照负载情况分成顺序读写、随机读写两大类。`fio` 是一个可以产生很多线程或进程并执行用户指定的特定类型I/O操作的工具，`fio` 的典型用法是编译和模拟的I/O负载匹配的作业文件。也就是说 `fio` 是一个多线程 IO 生成工具，可以生成多种 IO 模式，用来测试磁盘设备的性能（也包括文件系统：如针对网络文件系统 NFS 的 IO 测试）

## 测试环境

- 发行版版本：openEuler 23.03 RISC-V Preview V1
- 内核版本：6.1.19
- 虚拟机版本：QEMU 8.0.2

### 与上游测试方式不同之处

- `fio` 从软件源直接获取而不是编译安装。
- 测试目录更改为当前目录下的 `test` 而不是创建新的文件系统执行。
- 测试文件大小改为 1G。

## 测试方法

见 [method.md](./method.md)。

## 测试结果

除了两块采用全志 D1 的开发板（荔枝派和哪吒）无法运行外，测试通过。QEMU 下 IO 性能表现良好。

测试结果详见 [log](./log) 目录下的日志文件。

QEMU 测试结果如下：

```
job1: (g=0): rw=read, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=10
...
fio-3.32
Starting 10 threads
job1: Laying out IO file (1 file / 1024MiB)
Jobs: 10 (f=10): [R(10)][100.0%][r=56.9MiB/s][r=14.6k IOPS][eta 00m:00s]
job1: (groupid=0, jobs=10): err= 0: pid=1416: Wed Apr 26 17:22:20 2023
  read: IOPS=14.8k, BW=57.8MiB/s (60.6MB/s)(1734MiB/30009msec)
    slat (usec): min=95, max=33271, avg=483.86, stdev=1317.10
    clat (usec): min=149, max=49114, avg=6239.27, stdev=4879.53
     lat (usec): min=443, max=56151, avg=6723.13, stdev=5096.72
    clat percentiles (usec):
     |  1.00th=[ 3425],  5.00th=[ 3752], 10.00th=[ 3916], 20.00th=[ 4146],
     | 30.00th=[ 4293], 40.00th=[ 4490], 50.00th=[ 4621], 60.00th=[ 4817],
     | 70.00th=[ 5080], 80.00th=[ 5407], 90.00th=[12125], 95.00th=[20317],
     | 99.00th=[27395], 99.50th=[29492], 99.90th=[34341], 99.95th=[37487],
     | 99.99th=[43254]
   bw (  KiB/s): min=23675, max=81268, per=100.00%, avg=59221.36, stdev=1646.05, samples=590
   iops        : min= 5916, max=20314, avg=14801.95, stdev=411.50, samples=590
  lat (usec)   : 250=0.01%, 500=0.01%, 750=0.01%, 1000=0.01%
  lat (msec)   : 2=0.01%, 4=13.05%, 10=75.14%, 20=6.40%, 50=5.40%
  cpu          : usr=8.91%, sys=70.26%, ctx=13204, majf=0, minf=110
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=100.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.1%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=443852,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=10

Run status group 0 (all jobs):
   READ: bw=57.8MiB/s (60.6MB/s), 57.8MiB/s-57.8MiB/s (60.6MB/s-60.6MB/s), io=1734MiB (1818MB), run=30009-30009msec

Disk stats (read/write):
  vda: ios=441771/2, merge=55/0, ticks=257706/2, in_queue=257707, util=99.81%
job1: (g=0): rw=read, bs=(R) 16.0KiB-16.0KiB, (W) 16.0KiB-16.0KiB, (T) 16.0KiB-16.0KiB, ioengine=libaio, iodepth=10
...
fio-3.32
Starting 10 threads
Jobs: 10 (f=0): [f(10)][100.0%][r=217MiB/s][r=13.9k IOPS][eta 00m:00s] 
job1: (groupid=0, jobs=10): err= 0: pid=1429: Wed Apr 26 17:23:21 2023
  read: IOPS=14.2k, BW=222MiB/s (233MB/s)(6673MiB/30002msec)
    slat (usec): min=98, max=33257, avg=503.13, stdev=1328.57
    clat (usec): min=98, max=59375, avg=6484.64, stdev=4967.57
     lat (usec): min=353, max=60014, avg=6987.77, stdev=5178.29
    clat percentiles (usec):
     |  1.00th=[ 3556],  5.00th=[ 3916], 10.00th=[ 4080], 20.00th=[ 4293],
     | 30.00th=[ 4490], 40.00th=[ 4686], 50.00th=[ 4817], 60.00th=[ 5014],
     | 70.00th=[ 5276], 80.00th=[ 5669], 90.00th=[12387], 95.00th=[20579],
     | 99.00th=[27395], 99.50th=[29492], 99.90th=[35914], 99.95th=[39060],
     | 99.99th=[44827]
   bw (  KiB/s): min=92507, max=316820, per=100.00%, avg=227933.97, stdev=6372.07, samples=590
   iops        : min= 5777, max=19798, avg=14241.47, stdev=398.24, samples=590
  lat (usec)   : 100=0.01%, 250=0.01%, 500=0.01%, 750=0.01%, 1000=0.01%
  lat (msec)   : 2=0.01%, 4=7.29%, 10=80.53%, 20=6.21%, 50=5.96%
  lat (msec)   : 100=0.01%
  cpu          : usr=8.32%, sys=70.76%, ctx=13281, majf=0, minf=410
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=100.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.1%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=427085,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=10

Run status group 0 (all jobs):
   READ: bw=222MiB/s (233MB/s), 222MiB/s-222MiB/s (233MB/s-233MB/s), io=6673MiB (6997MB), run=30002-30002msec

Disk stats (read/write):
  vda: ios=423906/0, merge=48/0, ticks=251076/0, in_queue=251076, util=99.82%
job1: (g=0): rw=read, bs=(R) 32.0KiB-32.0KiB, (W) 32.0KiB-32.0KiB, (T) 32.0KiB-32.0KiB, ioengine=libaio, iodepth=10
...
fio-3.32
Starting 10 threads
Jobs: 2 (f=2): [_(5),R(2),_(3)][96.2%][r=267MiB/s][r=8543 IOPS][eta 00m:01s]           
job1: (groupid=0, jobs=10): err= 0: pid=1442: Wed Apr 26 17:24:16 2023
  read: IOPS=13.3k, BW=416MiB/s (436MB/s)(10.0GiB/24628msec)
    slat (usec): min=109, max=37343, avg=507.30, stdev=1290.80
    clat (usec): min=155, max=57064, avg=6510.01, stdev=4799.60
     lat (usec): min=307, max=58788, avg=7017.31, stdev=5005.54
    clat percentiles (usec):
     |  1.00th=[ 3064],  5.00th=[ 3851], 10.00th=[ 4146], 20.00th=[ 4424],
     | 30.00th=[ 4621], 40.00th=[ 4752], 50.00th=[ 4948], 60.00th=[ 5145],
     | 70.00th=[ 5407], 80.00th=[ 5800], 90.00th=[12256], 95.00th=[20579],
     | 99.00th=[25822], 99.50th=[28967], 99.90th=[33817], 99.95th=[36963],
     | 99.99th=[44827]
   bw (  KiB/s): min=196682, max=709023, per=100.00%, avg=451448.63, stdev=12502.95, samples=453
   iops        : min= 6142, max=22152, avg=14103.28, stdev=390.72, samples=453
  lat (usec)   : 250=0.01%, 500=0.01%, 750=0.01%, 1000=0.01%
  lat (msec)   : 2=0.01%, 4=7.05%, 10=80.74%, 20=6.50%, 50=5.69%
  lat (msec)   : 100=0.01%
  cpu          : usr=8.73%, sys=71.32%, ctx=10134, majf=0, minf=810
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=100.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.1%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=327680,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=10

Run status group 0 (all jobs):
   READ: bw=416MiB/s (436MB/s), 416MiB/s-416MiB/s (436MB/s-436MB/s), io=10.0GiB (10.7GB), run=24628-24628msec

Disk stats (read/write):
  vda: ios=327151/0, merge=45/0, ticks=188789/0, in_queue=188789, util=99.74%
job1: (g=0): rw=read, bs=(R) 64.0KiB-64.0KiB, (W) 64.0KiB-64.0KiB, (T) 64.0KiB-64.0KiB, ioengine=libaio, iodepth=10
...
fio-3.32
Starting 10 threads
Jobs: 2 (f=2): [R(1),_(3),R(1),_(5)][94.1%][r=586MiB/s][r=9377 IOPS][eta 00m:01s]           
job1: (groupid=0, jobs=10): err= 0: pid=1455: Wed Apr 26 17:25:02 2023
  read: IOPS=10.7k, BW=670MiB/s (702MB/s)(10.0GiB/15293msec)
    slat (usec): min=114, max=32844, avg=631.96, stdev=1351.62
    clat (usec): min=163, max=68472, avg=7469.93, stdev=5439.45
     lat (usec): min=324, max=71803, avg=8101.88, stdev=5769.26
    clat percentiles (usec):
     |  1.00th=[ 2933],  5.00th=[ 3523], 10.00th=[ 3884], 20.00th=[ 4293],
     | 30.00th=[ 4621], 40.00th=[ 5014], 50.00th=[ 5604], 60.00th=[ 6718],
     | 70.00th=[ 7570], 80.00th=[ 8455], 90.00th=[13042], 95.00th=[20841],
     | 99.00th=[28443], 99.50th=[32637], 99.90th=[42730], 99.95th=[47973],
     | 99.99th=[54789]
   bw (  KiB/s): min=344071, max=1480452, per=100.00%, avg=793193.10, stdev=31771.48, samples=261
   iops        : min= 5370, max=23126, avg=12388.90, stdev=496.43, samples=261
  lat (usec)   : 250=0.01%, 500=0.01%, 750=0.01%, 1000=0.01%
  lat (msec)   : 2=0.02%, 4=12.76%, 10=74.72%, 20=6.13%, 50=6.32%
  lat (msec)   : 100=0.04%
  cpu          : usr=8.02%, sys=75.04%, ctx=5412, majf=0, minf=607
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=100.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.1%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=163840,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=10

Run status group 0 (all jobs):
   READ: bw=670MiB/s (702MB/s), 670MiB/s-670MiB/s (702MB/s-702MB/s), io=10.0GiB (10.7GB), run=15293-15293msec

Disk stats (read/write):
  vda: ios=163110/0, merge=60/0, ticks=71693/0, in_queue=71692, util=99.43%
job1: (g=0): rw=read, bs=(R) 128KiB-128KiB, (W) 128KiB-128KiB, (T) 128KiB-128KiB, ioengine=libaio, iodepth=10
...
fio-3.32
Starting 10 threads
Jobs: 5 (f=3): [_(2),R(2),_(1),R(1),f(1),_(2),f(1)][83.3%][r=849MiB/s][r=6794 IOPS][eta 00m:02s]
job1: (groupid=0, jobs=10): err= 0: pid=1468: Wed Apr 26 17:25:42 2023
  read: IOPS=8548, BW=1069MiB/s (1120MB/s)(10.0GiB/9583msec)
    slat (usec): min=129, max=34609, avg=764.41, stdev=1430.51
    clat (usec): min=115, max=70253, avg=8631.84, stdev=5977.18
     lat (usec): min=280, max=72748, avg=9396.25, stdev=6377.50
    clat percentiles (usec):
     |  1.00th=[ 3032],  5.00th=[ 3818], 10.00th=[ 4293], 20.00th=[ 4817],
     | 30.00th=[ 5276], 40.00th=[ 6063], 50.00th=[ 7177], 60.00th=[ 8094],
     | 70.00th=[ 8979], 80.00th=[10290], 90.00th=[13304], 95.00th=[22676],
     | 99.00th=[31065], 99.50th=[38011], 99.90th=[54264], 99.95th=[56361],
     | 99.99th=[64226]
   bw (  MiB/s): min=  710, max= 2213, per=100.00%, avg=1355.44, stdev=43.93, samples=148
   iops        : min= 5680, max=17706, avg=10838.60, stdev=351.47, samples=148
  lat (usec)   : 250=0.01%, 500=0.01%, 750=0.01%, 1000=0.01%
  lat (msec)   : 2=0.03%, 4=6.26%, 10=71.85%, 20=14.54%, 50=7.12%
  lat (msec)   : 100=0.18%
  cpu          : usr=6.92%, sys=77.84%, ctx=2934, majf=0, minf=1687
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=99.9%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.1%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=81920,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=10

Run status group 0 (all jobs):
   READ: bw=1069MiB/s (1120MB/s), 1069MiB/s-1069MiB/s (1120MB/s-1120MB/s), io=10.0GiB (10.7GB), run=9583-9583msec

Disk stats (read/write):
  vda: ios=80804/0, merge=17/0, ticks=33840/0, in_queue=33840, util=98.94%
job1: (g=0): rw=read, bs=(R) 256KiB-256KiB, (W) 256KiB-256KiB, (T) 256KiB-256KiB, ioengine=libaio, iodepth=10
...
fio-3.32
Starting 10 threads
Jobs: 3 (f=0): [_(2),f(1),_(1),f(1),_(1),f(1),_(3)][100.0%][r=838MiB/s][r=3350 IOPS][eta 00m:00s]              
job1: (groupid=0, jobs=10): err= 0: pid=1483: Wed Apr 26 17:26:22 2023
  read: IOPS=4636, BW=1159MiB/s (1215MB/s)(10.0GiB/8835msec)
    slat (usec): min=170, max=30681, avg=1509.42, stdev=1867.80
    clat (usec): min=121, max=90765, avg=15242.01, stdev=8586.05
     lat (usec): min=417, max=106910, avg=16751.43, stdev=9381.20
    clat percentiles (usec):
     |  1.00th=[ 3982],  5.00th=[ 5014], 10.00th=[ 5932], 20.00th=[ 7898],
     | 30.00th=[10552], 40.00th=[13042], 50.00th=[14746], 60.00th=[16188],
     | 70.00th=[17433], 80.00th=[19268], 90.00th=[23725], 95.00th=[31327],
     | 99.00th=[50070], 99.50th=[54789], 99.90th=[67634], 99.95th=[76022],
     | 99.99th=[86508]
   bw (  MiB/s): min=  889, max= 2264, per=100.00%, avg=1587.24, stdev=38.41, samples=131
   iops        : min= 3555, max= 9053, avg=6343.78, stdev=153.60, samples=131
  lat (usec)   : 250=0.01%, 500=0.01%, 750=0.01%, 1000=0.01%
  lat (msec)   : 2=0.03%, 4=0.95%, 10=26.83%, 20=55.24%, 50=15.94%
  lat (msec)   : 100=0.97%
  cpu          : usr=4.95%, sys=82.68%, ctx=2170, majf=0, minf=1827
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=99.8%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.1%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=40960,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=10

Run status group 0 (all jobs):
   READ: bw=1159MiB/s (1215MB/s), 1159MiB/s-1159MiB/s (1215MB/s-1215MB/s), io=10.0GiB (10.7GB), run=8835-8835msec

Disk stats (read/write):
  vda: ios=40113/0, merge=3/0, ticks=14498/0, in_queue=14498, util=98.80%
job1: (g=0): rw=read, bs=(R) 512KiB-512KiB, (W) 512KiB-512KiB, (T) 512KiB-512KiB, ioengine=libaio, iodepth=10
...
fio-3.32
Starting 10 threads
Jobs: 5 (f=5): [R(1),_(2),R(4),_(3)][86.7%][r=675MiB/s][r=1350 IOPS][eta 00m:02s]          
job1: (groupid=0, jobs=10): err= 0: pid=1496: Wed Apr 26 17:27:05 2023
  read: IOPS=1620, BW=810MiB/s (850MB/s)(10.0GiB/12635msec)
    slat (usec): min=274, max=47789, avg=4878.08, stdev=4065.49
    clat (usec): min=149, max=179955, avg=45253.11, stdev=23560.11
     lat (usec): min=1266, max=187439, avg=50131.19, stdev=25893.63
    clat percentiles (msec):
     |  1.00th=[   12],  5.00th=[   16], 10.00th=[   21], 20.00th=[   28],
     | 30.00th=[   32], 40.00th=[   36], 50.00th=[   41], 60.00th=[   46],
     | 70.00th=[   54], 80.00th=[   59], 90.00th=[   72], 95.00th=[   95],
     | 99.00th=[  127], 99.50th=[  138], 99.90th=[  153], 99.95th=[  159],
     | 99.99th=[  171]
   bw (  MiB/s): min=  606, max= 1605, per=100.00%, avg=1090.87, stdev=27.48, samples=197
   iops        : min= 1209, max= 3205, avg=2176.96, stdev=54.93, samples=197
  lat (usec)   : 250=0.02%, 500=0.02%, 750=0.01%
  lat (msec)   : 2=0.01%, 4=0.02%, 10=0.20%, 20=9.71%, 50=56.42%
  lat (msec)   : 100=29.61%, 250=3.98%
  cpu          : usr=2.12%, sys=86.23%, ctx=2888, majf=0, minf=2600
  IO depths    : 1=0.1%, 2=0.1%, 4=0.2%, 8=99.7%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.1%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=20480,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=10

Run status group 0 (all jobs):
   READ: bw=810MiB/s (850MB/s), 810MiB/s-810MiB/s (850MB/s-850MB/s), io=10.0GiB (10.7GB), run=12635-12635msec

Disk stats (read/write):
  vda: ios=20089/0, merge=5/0, ticks=7406/0, in_queue=7406, util=98.55%
job1: (g=0): rw=read, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=10
...
fio-3.32
Starting 10 threads
Jobs: 8 (f=7): [R(7),_(2),f(1)][94.1%][r=576MiB/s][r=576 IOPS][eta 00m:01s] 
job1: (groupid=0, jobs=10): err= 0: pid=1509: Wed Apr 26 17:27:51 2023
  read: IOPS=666, BW=667MiB/s (699MB/s)(10.0GiB/15353msec)
    slat (usec): min=409, max=60910, avg=14244.77, stdev=6641.86
    clat (usec): min=267, max=273719, avg=128973.51, stdev=41225.05
     lat (msec): min=2, max=297, avg=143.22, stdev=44.82
    clat percentiles (msec):
     |  1.00th=[   35],  5.00th=[   86], 10.00th=[   91], 20.00th=[  105],
     | 30.00th=[  108], 40.00th=[  111], 50.00th=[  115], 60.00th=[  121],
     | 70.00th=[  136], 80.00th=[  161], 90.00th=[  199], 95.00th=[  218],
     | 99.00th=[  241], 99.50th=[  247], 99.90th=[  262], 99.95th=[  266],
     | 99.99th=[  271]
   bw (  KiB/s): min=380763, max=919488, per=100.00%, avg=700189.27, stdev=13334.06, samples=287
   iops        : min=  364, max=  894, avg=678.52, stdev=13.09, samples=287
  lat (usec)   : 500=0.07%, 750=0.01%
  lat (msec)   : 2=0.01%, 4=0.03%, 10=0.11%, 20=0.19%, 50=1.14%
  lat (msec)   : 100=12.46%, 250=85.65%, 500=0.33%
  cpu          : usr=0.77%, sys=80.77%, ctx=4866, majf=0, minf=1098
  IO depths    : 1=0.1%, 2=0.2%, 4=0.4%, 8=99.3%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=99.9%, 8=0.0%, 16=0.1%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=10240,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=10

Run status group 0 (all jobs):
   READ: bw=667MiB/s (699MB/s), 667MiB/s-667MiB/s (699MB/s-699MB/s), io=10.0GiB (10.7GB), run=15353-15353msec

Disk stats (read/write):
  vda: ios=10121/0, merge=0/0, ticks=3984/0, in_queue=3984, util=94.47%
job1: (g=0): rw=write, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=10
...
fio-3.32
Starting 10 threads
Jobs: 10 (f=0): [f(10)][100.0%][w=45.4MiB/s][w=11.6k IOPS][eta 00m:00s] 
job1: (groupid=0, jobs=10): err= 0: pid=1522: Wed Apr 26 17:28:51 2023
  write: IOPS=12.2k, BW=47.8MiB/s (50.1MB/s)(1434MiB/30007msec); 0 zone resets
    slat (usec): min=97, max=67741, avg=542.60, stdev=785.47
    clat (usec): min=222, max=130911, avg=7578.40, stdev=7920.93
     lat (usec): min=434, max=147889, avg=8121.00, stdev=8287.43
    clat percentiles (usec):
     |  1.00th=[ 4047],  5.00th=[ 4424], 10.00th=[ 4686], 20.00th=[ 4948],
     | 30.00th=[ 5145], 40.00th=[ 5342], 50.00th=[ 5604], 60.00th=[ 5800],
     | 70.00th=[ 6063], 80.00th=[ 6521], 90.00th=[ 9634], 95.00th=[15664],
     | 99.00th=[49021], 99.50th=[53740], 99.90th=[62653], 99.95th=[66847],
     | 99.99th=[83362]
   bw (  KiB/s): min= 8351, max=70571, per=100.00%, avg=48972.97, stdev=2205.99, samples=590
   iops        : min= 2082, max=17639, avg=12239.37, stdev=551.50, samples=590
  lat (usec)   : 250=0.01%, 500=0.01%, 750=0.01%, 1000=0.01%
  lat (msec)   : 2=0.01%, 4=0.74%, 10=89.89%, 20=4.60%, 50=3.91%
  lat (msec)   : 100=0.84%, 250=0.01%
  cpu          : usr=8.21%, sys=61.41%, ctx=305525, majf=0, minf=10
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=100.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.1%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=0,367078,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=10

Run status group 0 (all jobs):
  WRITE: bw=47.8MiB/s (50.1MB/s), 47.8MiB/s-47.8MiB/s (50.1MB/s-50.1MB/s), io=1434MiB (1504MB), run=30007-30007msec

Disk stats (read/write):
  vda: ios=0/364411, merge=0/76, ticks=0/231408, in_queue=231586, util=99.68%
job1: (g=0): rw=write, bs=(R) 16.0KiB-16.0KiB, (W) 16.0KiB-16.0KiB, (T) 16.0KiB-16.0KiB, ioengine=libaio, iodepth=10
...
fio-3.32
Starting 10 threads
Jobs: 10 (f=0): [f(10)][100.0%][w=182MiB/s][w=11.6k IOPS][eta 00m:00s] 
job1: (groupid=0, jobs=10): err= 0: pid=1544: Wed Apr 26 17:29:52 2023
  write: IOPS=12.4k, BW=194MiB/s (203MB/s)(5818MiB/30012msec); 0 zone resets
    slat (usec): min=105, max=23900, avg=526.61, stdev=724.86
    clat (usec): min=252, max=80178, avg=7481.37, stdev=8121.63
     lat (usec): min=507, max=86252, avg=8007.98, stdev=8474.74
    clat percentiles (usec):
     |  1.00th=[ 4080],  5.00th=[ 4424], 10.00th=[ 4686], 20.00th=[ 4948],
     | 30.00th=[ 5145], 40.00th=[ 5342], 50.00th=[ 5473], 60.00th=[ 5669],
     | 70.00th=[ 5932], 80.00th=[ 6259], 90.00th=[ 7308], 95.00th=[23462],
     | 99.00th=[48497], 99.50th=[52167], 99.90th=[59507], 99.95th=[62129],
     | 99.99th=[67634]
   bw (  KiB/s): min=58106, max=284358, per=100.00%, avg=198781.08, stdev=9303.46, samples=590
   iops        : min= 3627, max=17769, avg=12419.15, stdev=581.45, samples=590
  lat (usec)   : 500=0.01%, 750=0.01%, 1000=0.01%
  lat (msec)   : 2=0.01%, 4=0.66%, 10=91.86%, 20=2.37%, 50=4.34%
  lat (msec)   : 100=0.76%
  cpu          : usr=8.34%, sys=61.41%, ctx=315583, majf=0, minf=10
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=100.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.1%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=0,372348,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=10

Run status group 0 (all jobs):
  WRITE: bw=194MiB/s (203MB/s), 194MiB/s-194MiB/s (203MB/s-203MB/s), io=5818MiB (6101MB), run=30012-30012msec

Disk stats (read/write):
  vda: ios=0/369648, merge=0/58, ticks=0/224753, in_queue=225098, util=99.78%
job1: (g=0): rw=write, bs=(R) 32.0KiB-32.0KiB, (W) 32.0KiB-32.0KiB, (T) 32.0KiB-32.0KiB, ioengine=libaio, iodepth=10
...
fio-3.32
Starting 10 threads
Jobs: 1 (f=1): [_(6),W(1),_(3)][100.0%][w=90.2MiB/s][w=2885 IOPS][eta 00m:00s]                        
job1: (groupid=0, jobs=10): err= 0: pid=1557: Wed Apr 26 17:30:52 2023
  write: IOPS=11.3k, BW=352MiB/s (369MB/s)(10.0GiB/29120msec); 0 zone resets
    slat (usec): min=114, max=28506, avg=535.30, stdev=660.01
    clat (usec): min=245, max=80255, avg=7313.66, stdev=7012.68
     lat (usec): min=562, max=81822, avg=7848.96, stdev=7334.71
    clat percentiles (usec):
     |  1.00th=[ 3294],  5.00th=[ 4113], 10.00th=[ 4555], 20.00th=[ 4948],
     | 30.00th=[ 5211], 40.00th=[ 5407], 50.00th=[ 5604], 60.00th=[ 5866],
     | 70.00th=[ 6128], 80.00th=[ 6587], 90.00th=[ 9765], 95.00th=[13829],
     | 99.00th=[45876], 99.50th=[50594], 99.90th=[57934], 99.95th=[61080],
     | 99.99th=[67634]
   bw (  KiB/s): min=64821, max=654056, per=100.00%, avg=405014.76, stdev=18175.91, samples=508
   iops        : min= 2020, max=20436, avg=12652.09, stdev=568.00, samples=508
  lat (usec)   : 250=0.01%, 500=0.01%, 750=0.01%, 1000=0.01%
  lat (msec)   : 2=0.01%, 4=4.23%, 10=86.06%, 20=5.59%, 50=3.58%
  lat (msec)   : 100=0.53%
  cpu          : usr=8.49%, sys=62.68%, ctx=283116, majf=0, minf=10
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=100.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.1%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=0,327680,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=10

Run status group 0 (all jobs):
  WRITE: bw=352MiB/s (369MB/s), 352MiB/s-352MiB/s (369MB/s-369MB/s), io=10.0GiB (10.7GB), run=29120-29120msec

Disk stats (read/write):
  vda: ios=0/327331, merge=0/39, ticks=0/195036, in_queue=195571, util=99.76%
job1: (g=0): rw=write, bs=(R) 64.0KiB-64.0KiB, (W) 64.0KiB-64.0KiB, (T) 64.0KiB-64.0KiB, ioengine=libaio, iodepth=10
...
fio-3.32
Starting 10 threads
Jobs: 2 (f=2): [W(1),_(8),W(1)][94.1%][w=407MiB/s][w=6515 IOPS][eta 00m:01s]                    
job1: (groupid=0, jobs=10): err= 0: pid=1570: Wed Apr 26 17:31:37 2023
  write: IOPS=10.7k, BW=669MiB/s (702MB/s)(10.0GiB/15302msec); 0 zone resets
    slat (usec): min=125, max=32083, avg=545.77, stdev=631.07
    clat (usec): min=132, max=109113, avg=7161.85, stdev=6956.01
     lat (usec): min=379, max=113179, avg=7707.62, stdev=7295.46
    clat percentiles (usec):
     |  1.00th=[ 3425],  5.00th=[ 3884], 10.00th=[ 4228], 20.00th=[ 4752],
     | 30.00th=[ 5080], 40.00th=[ 5342], 50.00th=[ 5538], 60.00th=[ 5800],
     | 70.00th=[ 6128], 80.00th=[ 6718], 90.00th=[ 9110], 95.00th=[14222],
     | 99.00th=[45351], 99.50th=[54789], 99.90th=[65799], 99.95th=[69731],
     | 99.99th=[79168]
   bw (  KiB/s): min=271735, max=1286805, per=100.00%, avg=837792.36, stdev=36202.91, samples=246
   iops        : min= 4242, max=20102, avg=13085.83, stdev=565.68, samples=246
  lat (usec)   : 250=0.01%, 500=0.01%, 750=0.01%, 1000=0.01%
  lat (msec)   : 2=0.02%, 4=6.38%, 10=84.55%, 20=5.43%, 50=2.88%
  lat (msec)   : 100=0.72%, 250=0.01%
  cpu          : usr=8.64%, sys=64.25%, ctx=150649, majf=0, minf=13
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=100.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.1%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=0,163840,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=10

Run status group 0 (all jobs):
  WRITE: bw=669MiB/s (702MB/s), 669MiB/s-669MiB/s (702MB/s-702MB/s), io=10.0GiB (10.7GB), run=15302-15302msec

Disk stats (read/write):
  vda: ios=0/163192, merge=0/41, ticks=0/84557, in_queue=84951, util=99.34%
job1: (g=0): rw=write, bs=(R) 128KiB-128KiB, (W) 128KiB-128KiB, (T) 128KiB-128KiB, ioengine=libaio, iodepth=10
...
fio-3.32
Starting 10 threads
Jobs: 3 (f=3): [_(1),W(1),_(1),W(1),_(1),W(1),_(4)][91.7%][w=580MiB/s][w=4640 IOPS][eta 00m:01s]
job1: (groupid=0, jobs=10): err= 0: pid=1583: Wed Apr 26 17:32:18 2023
  write: IOPS=7864, BW=983MiB/s (1031MB/s)(10.0GiB/10416msec); 0 zone resets
    slat (usec): min=150, max=16733, avg=735.23, stdev=616.54
    clat (usec): min=211, max=64572, avg=8768.40, stdev=5583.40
     lat (usec): min=588, max=65400, avg=9503.63, stdev=5945.64
    clat percentiles (usec):
     |  1.00th=[ 3916],  5.00th=[ 4752], 10.00th=[ 5145], 20.00th=[ 5538],
     | 30.00th=[ 5866], 40.00th=[ 6259], 50.00th=[ 6718], 60.00th=[ 7504],
     | 70.00th=[ 8717], 80.00th=[10290], 90.00th=[15664], 95.00th=[19268],
     | 99.00th=[33817], 99.50th=[39060], 99.90th=[47973], 99.95th=[50070],
     | 99.99th=[55313]
   bw (  MiB/s): min=  735, max= 1909, per=100.00%, avg=1380.21, stdev=40.77, samples=149
   iops        : min= 5877, max=15268, avg=11037.11, stdev=326.09, samples=149
  lat (usec)   : 250=0.01%, 500=0.01%, 750=0.01%, 1000=0.01%
  lat (msec)   : 2=0.02%, 4=1.09%, 10=77.36%, 20=17.14%, 50=4.31%
  lat (msec)   : 100=0.05%
  cpu          : usr=9.10%, sys=66.29%, ctx=78809, majf=0, minf=11
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=99.9%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.1%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=0,81920,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=10

Run status group 0 (all jobs):
  WRITE: bw=983MiB/s (1031MB/s), 983MiB/s-983MiB/s (1031MB/s-1031MB/s), io=10.0GiB (10.7GB), run=10416-10416msec

Disk stats (read/write):
  vda: ios=0/81799, merge=0/20, ticks=0/42076, in_queue=42439, util=99.05%
job1: (g=0): rw=write, bs=(R) 256KiB-256KiB, (W) 256KiB-256KiB, (T) 256KiB-256KiB, ioengine=libaio, iodepth=10
...
fio-3.32
Starting 10 threads
Jobs: 4 (f=4): [_(1),W(1),_(3),W(3),_(2)][86.7%][w=796MiB/s][w=3183 IOPS][eta 00m:02s]
job1: (groupid=0, jobs=10): err= 0: pid=1596: Wed Apr 26 17:33:01 2023
  write: IOPS=3246, BW=812MiB/s (851MB/s)(10.0GiB/12615msec); 0 zone resets
    slat (usec): min=202, max=18512, avg=2253.83, stdev=1645.33
    clat (usec): min=225, max=99155, avg=22406.21, stdev=12118.42
     lat (usec): min=808, max=106346, avg=24660.04, stdev=13235.18
    clat percentiles (usec):
     |  1.00th=[ 4948],  5.00th=[ 5932], 10.00th=[ 8094], 20.00th=[12256],
     | 30.00th=[14484], 40.00th=[17171], 50.00th=[21627], 60.00th=[25297],
     | 70.00th=[27919], 80.00th=[30802], 90.00th=[34341], 95.00th=[45876],
     | 99.00th=[63177], 99.50th=[67634], 99.90th=[80217], 99.95th=[82314],
     | 99.99th=[89654]
   bw (  MiB/s): min=  753, max= 1988, per=100.00%, avg=1203.39, stdev=31.49, samples=195
   iops        : min= 3010, max= 7950, avg=4808.71, stdev=125.96, samples=195
  lat (usec)   : 250=0.01%, 500=0.01%, 750=0.01%, 1000=0.01%
  lat (msec)   : 2=0.03%, 4=0.05%, 10=13.38%, 20=33.38%, 50=49.29%
  lat (msec)   : 100=3.84%
  cpu          : usr=4.78%, sys=80.95%, ctx=42633, majf=0, minf=10
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=99.8%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.1%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=0,40960,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=10

Run status group 0 (all jobs):
  WRITE: bw=812MiB/s (851MB/s), 812MiB/s-812MiB/s (851MB/s-851MB/s), io=10.0GiB (10.7GB), run=12615-12615msec

Disk stats (read/write):
  vda: ios=0/40951, merge=0/14, ticks=0/17206, in_queue=17595, util=99.17%
job1: (g=0): rw=write, bs=(R) 512KiB-512KiB, (W) 512KiB-512KiB, (T) 512KiB-512KiB, ioengine=libaio, iodepth=10
...
fio-3.32
Starting 10 threads
Jobs: 1 (f=1): [_(7),W(1),_(2)][100.0%][w=739MiB/s][w=1477 IOPS][eta 00m:00s]                        
job1: (groupid=0, jobs=10): err= 0: pid=1609: Wed Apr 26 17:33:43 2023
  write: IOPS=1868, BW=934MiB/s (979MB/s)(10.0GiB/10963msec); 0 zone resets
    slat (usec): min=291, max=19763, avg=4079.30, stdev=2898.04
    clat (usec): min=275, max=123351, avg=38324.35, stdev=17411.91
     lat (usec): min=747, max=129737, avg=42403.65, stdev=19103.14
    clat percentiles (msec):
     |  1.00th=[   11],  5.00th=[   12], 10.00th=[   14], 20.00th=[   21],
     | 30.00th=[   31], 40.00th=[   36], 50.00th=[   40], 60.00th=[   44],
     | 70.00th=[   48], 80.00th=[   52], 90.00th=[   58], 95.00th=[   66],
     | 99.00th=[   88], 99.50th=[   93], 99.90th=[  104], 99.95th=[  108],
     | 99.99th=[  118]
   bw (  MiB/s): min=  954, max= 1794, per=100.00%, avg=1380.49, stdev=22.72, samples=164
   iops        : min= 1906, max= 3585, avg=2755.64, stdev=45.44, samples=164
  lat (usec)   : 500=0.03%, 750=0.01%, 1000=0.01%
  lat (msec)   : 2=0.01%, 4=0.04%, 10=0.83%, 20=18.68%, 50=57.19%
  lat (msec)   : 100=23.07%, 250=0.15%
  cpu          : usr=4.22%, sys=84.32%, ctx=22220, majf=0, minf=10
  IO depths    : 1=0.1%, 2=0.1%, 4=0.2%, 8=99.7%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.1%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=0,20480,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=10

Run status group 0 (all jobs):
  WRITE: bw=934MiB/s (979MB/s), 934MiB/s-934MiB/s (979MB/s-979MB/s), io=10.0GiB (10.7GB), run=10963-10963msec

Disk stats (read/write):
  vda: ios=0/20385, merge=0/6, ticks=0/8914, in_queue=9231, util=98.65%
job1: (g=0): rw=write, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=10
...
fio-3.32
Starting 10 threads
Jobs: 4 (f=4): [_(3),W(2),_(2),W(2),_(1)][88.9%][w=731MiB/s][w=730 IOPS][eta 00m:02s]
job1: (groupid=0, jobs=10): err= 0: pid=1622: Wed Apr 26 17:34:29 2023
  write: IOPS=659, BW=659MiB/s (691MB/s)(10.0GiB/15534msec); 0 zone resets
    slat (usec): min=606, max=56890, avg=14147.49, stdev=8559.68
    clat (usec): min=334, max=286402, avg=129446.01, stdev=47629.67
     lat (msec): min=2, max=321, avg=143.59, stdev=51.67
    clat percentiles (msec):
     |  1.00th=[   29],  5.00th=[   49], 10.00th=[   95], 20.00th=[  100],
     | 30.00th=[  104], 40.00th=[  109], 50.00th=[  117], 60.00th=[  126],
     | 70.00th=[  138], 80.00th=[  171], 90.00th=[  203], 95.00th=[  222],
     | 99.00th=[  259], 99.50th=[  266], 99.90th=[  279], 99.95th=[  279],
     | 99.99th=[  284]
   bw (  KiB/s): min=372222, max=1209962, per=100.00%, avg=686210.07, stdev=17636.52, samples=286
   iops        : min=  356, max= 1177, avg=664.75, stdev=17.28, samples=286
  lat (usec)   : 500=0.02%, 750=0.04%, 1000=0.03%
  lat (msec)   : 2=0.01%, 4=0.03%, 10=0.09%, 20=0.22%, 50=4.95%
  lat (msec)   : 100=15.89%, 250=77.12%, 500=1.60%
  cpu          : usr=1.81%, sys=77.14%, ctx=14141, majf=0, minf=10
  IO depths    : 1=0.1%, 2=0.2%, 4=0.4%, 8=99.3%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=99.9%, 8=0.0%, 16=0.1%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=0,10240,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=10

Run status group 0 (all jobs):
  WRITE: bw=659MiB/s (691MB/s), 659MiB/s-659MiB/s (691MB/s-691MB/s), io=10.0GiB (10.7GB), run=15534-15534msec

Disk stats (read/write):
  vda: ios=0/10155, merge=0/3, ticks=0/8426, in_queue=8771, util=91.51%
job1: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=10
...
fio-3.32
Starting 10 threads
Jobs: 2 (f=0): [E(6),f(1),E(1),f(1),E(1)][100.0%][r=49.7MiB/s][r=12.7k IOPS][eta 00m:00s]
job1: (groupid=0, jobs=10): err= 0: pid=1635: Wed Apr 26 17:35:30 2023
  read: IOPS=13.4k, BW=52.5MiB/s (55.0MB/s)(1574MiB/30010msec)
    slat (usec): min=97, max=33999, avg=526.17, stdev=1368.49
    clat (usec): min=95, max=53814, avg=6872.29, stdev=5124.56
     lat (usec): min=418, max=55977, avg=7398.45, stdev=5340.64
    clat percentiles (usec):
     |  1.00th=[ 3687],  5.00th=[ 4047], 10.00th=[ 4228], 20.00th=[ 4490],
     | 30.00th=[ 4752], 40.00th=[ 4883], 50.00th=[ 5145], 60.00th=[ 5342],
     | 70.00th=[ 5669], 80.00th=[ 6194], 90.00th=[13566], 95.00th=[20841],
     | 99.00th=[28181], 99.50th=[30540], 99.90th=[37487], 99.95th=[40109],
     | 99.99th=[47449]
   bw (  KiB/s): min=23577, max=75161, per=100.00%, avg=53774.54, stdev=1460.30, samples=590
   iops        : min= 5891, max=18785, avg=13439.73, stdev=365.07, samples=590
  lat (usec)   : 100=0.01%, 250=0.01%, 500=0.01%, 750=0.01%, 1000=0.01%
  lat (msec)   : 2=0.01%, 4=4.13%, 10=82.84%, 20=6.72%, 50=6.30%
  lat (msec)   : 100=0.01%
  cpu          : usr=9.20%, sys=69.85%, ctx=13167, majf=0, minf=110
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=100.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.1%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=402954,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=10

Run status group 0 (all jobs):
   READ: bw=52.5MiB/s (55.0MB/s), 52.5MiB/s-52.5MiB/s (55.0MB/s-55.0MB/s), io=1574MiB (1650MB), run=30010-30010msec

Disk stats (read/write):
  vda: ios=400192/0, merge=1/0, ticks=259909/0, in_queue=259909, util=99.79%
job1: (g=0): rw=randread, bs=(R) 16.0KiB-16.0KiB, (W) 16.0KiB-16.0KiB, (T) 16.0KiB-16.0KiB, ioengine=libaio, iodepth=10
...
fio-3.32
Starting 10 threads
Jobs: 10 (f=0): [f(10)][100.0%][r=200MiB/s][r=12.8k IOPS][eta 00m:00s] 
job1: (groupid=0, jobs=10): err= 0: pid=1649: Wed Apr 26 17:36:30 2023
  read: IOPS=12.8k, BW=200MiB/s (210MB/s)(6007MiB/30007msec)
    slat (usec): min=104, max=34010, avg=557.60, stdev=1413.98
    clat (usec): min=174, max=57355, avg=7200.42, stdev=5288.71
     lat (usec): min=419, max=61168, avg=7758.02, stdev=5517.01
    clat percentiles (usec):
     |  1.00th=[ 3884],  5.00th=[ 4228], 10.00th=[ 4490], 20.00th=[ 4752],
     | 30.00th=[ 4948], 40.00th=[ 5145], 50.00th=[ 5342], 60.00th=[ 5604],
     | 70.00th=[ 5932], 80.00th=[ 6456], 90.00th=[14353], 95.00th=[21103],
     | 99.00th=[28967], 99.50th=[31065], 99.90th=[38011], 99.95th=[42206],
     | 99.99th=[50594]
   bw (  KiB/s): min=83505, max=287917, per=100.00%, avg=205097.34, stdev=5711.49, samples=590
   iops        : min= 5215, max=17990, avg=12814.05, stdev=356.99, samples=590
  lat (usec)   : 250=0.01%, 500=0.01%, 750=0.01%, 1000=0.01%
  lat (msec)   : 2=0.01%, 4=1.70%, 10=84.86%, 20=6.49%, 50=6.93%
  lat (msec)   : 100=0.01%
  cpu          : usr=8.94%, sys=70.06%, ctx=13345, majf=0, minf=410
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=100.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.1%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=384443,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=10

Run status group 0 (all jobs):
   READ: bw=200MiB/s (210MB/s), 200MiB/s-200MiB/s (210MB/s-210MB/s), io=6007MiB (6299MB), run=30007-30007msec

Disk stats (read/write):
  vda: ios=381601/0, merge=4/0, ticks=251040/0, in_queue=251040, util=99.78%
job1: (g=0): rw=randread, bs=(R) 32.0KiB-32.0KiB, (W) 32.0KiB-32.0KiB, (T) 32.0KiB-32.0KiB, ioengine=libaio, iodepth=10
...
fio-3.32
Starting 10 threads
Jobs: 2 (f=1): [_(3),f(1),r(1),_(5)][100.0%][r=224MiB/s][r=7183 IOPS][eta 00m:00s]     
job1: (groupid=0, jobs=10): err= 0: pid=1662: Wed Apr 26 17:37:28 2023
  read: IOPS=12.0k, BW=375MiB/s (393MB/s)(10.0GiB/27288msec)
    slat (usec): min=111, max=37263, avg=567.12, stdev=1380.38
    clat (usec): min=248, max=63898, avg=7309.98, stdev=5254.07
     lat (usec): min=572, max=65314, avg=7877.10, stdev=5487.20
    clat percentiles (usec):
     |  1.00th=[ 3720],  5.00th=[ 4293], 10.00th=[ 4490], 20.00th=[ 4817],
     | 30.00th=[ 5014], 40.00th=[ 5276], 50.00th=[ 5538], 60.00th=[ 5800],
     | 70.00th=[ 6194], 80.00th=[ 6915], 90.00th=[13960], 95.00th=[21103],
     | 99.00th=[28705], 99.50th=[31327], 99.90th=[39060], 99.95th=[43254],
     | 99.99th=[54789]
   bw (  KiB/s): min=164881, max=597869, per=100.00%, avg=402693.04, stdev=11412.64, samples=510
   iops        : min= 5149, max=18679, avg=12579.38, stdev=356.65, samples=510
  lat (usec)   : 250=0.01%, 500=0.01%, 750=0.01%, 1000=0.01%
  lat (msec)   : 2=0.01%, 4=2.14%, 10=84.67%, 20=6.57%, 50=6.59%
  lat (msec)   : 100=0.02%
  cpu          : usr=9.14%, sys=71.13%, ctx=11264, majf=0, minf=810
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=100.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.1%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=327680,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=10

Run status group 0 (all jobs):
   READ: bw=375MiB/s (393MB/s), 375MiB/s-375MiB/s (393MB/s-393MB/s), io=10.0GiB (10.7GB), run=27288-27288msec

Disk stats (read/write):
  vda: ios=326885/12, merge=2/13, ticks=210276/31, in_queue=210331, util=99.76%
job1: (g=0): rw=randread, bs=(R) 64.0KiB-64.0KiB, (W) 64.0KiB-64.0KiB, (T) 64.0KiB-64.0KiB, ioengine=libaio, iodepth=10
...
fio-3.32
Starting 10 threads
Jobs: 5 (f=5): [r(1),_(1),r(1),_(1),r(1),_(1),r(2),_(2)][93.3%][r=728MiB/s][r=11.6k IOPS][eta 00m:01s]
job1: (groupid=0, jobs=10): err= 0: pid=1675: Wed Apr 26 17:38:12 2023
  read: IOPS=11.9k, BW=745MiB/s (781MB/s)(10.0GiB/13751msec)
    slat (usec): min=122, max=33601, avg=571.17, stdev=1364.38
    clat (usec): min=77, max=53639, avg=7261.05, stdev=5159.13
     lat (usec): min=299, max=55614, avg=7832.22, stdev=5383.87
    clat percentiles (usec):
     |  1.00th=[ 3556],  5.00th=[ 4178], 10.00th=[ 4490], 20.00th=[ 4883],
     | 30.00th=[ 5080], 40.00th=[ 5342], 50.00th=[ 5538], 60.00th=[ 5800],
     | 70.00th=[ 6128], 80.00th=[ 6718], 90.00th=[13960], 95.00th=[21365],
     | 99.00th=[28443], 99.50th=[31851], 99.90th=[38011], 99.95th=[41681],
     | 99.99th=[47449]
   bw (  KiB/s): min=382370, max=1236412, per=100.00%, avg=806356.49, stdev=23116.23, samples=251
   iops        : min= 5971, max=19315, avg=12594.77, stdev=361.18, samples=251
  lat (usec)   : 100=0.01%, 250=0.01%, 500=0.01%, 750=0.01%, 1000=0.01%
  lat (msec)   : 2=0.01%, 4=3.29%, 10=83.58%, 20=6.68%, 50=6.42%
  lat (msec)   : 100=0.01%
  cpu          : usr=8.49%, sys=71.89%, ctx=5720, majf=0, minf=1610
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=100.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.1%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=163840,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=10

Run status group 0 (all jobs):
   READ: bw=745MiB/s (781MB/s), 745MiB/s-745MiB/s (781MB/s-781MB/s), io=10.0GiB (10.7GB), run=13751-13751msec

Disk stats (read/write):
  vda: ios=163505/0, merge=2/0, ticks=99843/0, in_queue=99843, util=99.30%
job1: (g=0): rw=randread, bs=(R) 128KiB-128KiB, (W) 128KiB-128KiB, (T) 128KiB-128KiB, ioengine=libaio, iodepth=10
...
fio-3.32
Starting 10 threads
Jobs: 3 (f=3): [_(3),r(1),_(1),r(2),_(3)][81.8%][r=822MiB/s][r=6579 IOPS][eta 00m:02s]   
job1: (groupid=0, jobs=10): err= 0: pid=1688: Wed Apr 26 17:38:52 2023
  read: IOPS=9362, BW=1170MiB/s (1227MB/s)(10.0GiB/8750msec)
    slat (usec): min=130, max=29570, avg=696.00, stdev=1485.05
    clat (usec): min=115, max=67992, avg=8261.13, stdev=5770.01
     lat (usec): min=321, max=69900, avg=8957.12, stdev=6075.94
    clat percentiles (usec):
     |  1.00th=[ 2900],  5.00th=[ 4424], 10.00th=[ 4686], 20.00th=[ 5080],
     | 30.00th=[ 5407], 40.00th=[ 5669], 50.00th=[ 6063], 60.00th=[ 6587],
     | 70.00th=[ 7635], 80.00th=[ 9241], 90.00th=[16909], 95.00th=[22414],
     | 99.00th=[29754], 99.50th=[33162], 99.90th=[40633], 99.95th=[44827],
     | 99.99th=[56361]
   bw (  MiB/s): min=  693, max= 2144, per=100.00%, avg=1368.12, stdev=45.35, samples=141
   iops        : min= 5548, max=17155, avg=10940.30, stdev=362.75, samples=141
  lat (usec)   : 250=0.01%, 500=0.01%, 750=0.01%, 1000=0.01%
  lat (msec)   : 2=0.02%, 4=2.58%, 10=80.50%, 20=8.57%, 50=8.27%
  lat (msec)   : 100=0.03%
  cpu          : usr=7.73%, sys=72.79%, ctx=3158, majf=0, minf=2701
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=99.9%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.1%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=81920,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=10

Run status group 0 (all jobs):
   READ: bw=1170MiB/s (1227MB/s), 1170MiB/s-1170MiB/s (1227MB/s-1227MB/s), io=10.0GiB (10.7GB), run=8750-8750msec

Disk stats (read/write):
  vda: ios=81407/0, merge=1/0, ticks=40103/0, in_queue=40103, util=98.76%
job1: (g=0): rw=randread, bs=(R) 256KiB-256KiB, (W) 256KiB-256KiB, (T) 256KiB-256KiB, ioengine=libaio, iodepth=10
...
fio-3.32
Starting 10 threads
Jobs: 6 (f=5): [_(1),r(4),f(1),_(2),r(1),_(1)][87.5%][r=731MiB/s][r=2922 IOPS][eta 00m:02s]
job1: (groupid=0, jobs=10): err= 0: pid=1701: Wed Apr 26 17:39:36 2023
  read: IOPS=3012, BW=753MiB/s (790MB/s)(10.0GiB/13596msec)
    slat (usec): min=175, max=33543, avg=2744.58, stdev=2877.14
    clat (usec): min=168, max=92595, avg=26339.17, stdev=12802.64
     lat (usec): min=813, max=96595, avg=29083.75, stdev=13974.70
    clat percentiles (usec):
     |  1.00th=[ 7242],  5.00th=[10159], 10.00th=[11994], 20.00th=[15533],
     | 30.00th=[18220], 40.00th=[22938], 50.00th=[25560], 60.00th=[28181],
     | 70.00th=[30278], 80.00th=[32375], 90.00th=[39584], 95.00th=[56886],
     | 99.00th=[67634], 99.50th=[73925], 99.90th=[83362], 99.95th=[85459],
     | 99.99th=[87557]
   bw (  KiB/s): min=518683, max=1567431, per=100.00%, avg=902344.65, stdev=26215.15, samples=232
   iops        : min= 2021, max= 6118, avg=3520.05, stdev=102.42, samples=232
  lat (usec)   : 250=0.01%, 500=0.01%, 750=0.01%, 1000=0.01%
  lat (msec)   : 2=0.03%, 4=0.06%, 10=4.60%, 20=29.48%, 50=59.11%
  lat (msec)   : 100=6.70%
  cpu          : usr=3.12%, sys=82.42%, ctx=3921, majf=0, minf=1823
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=99.8%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.1%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=40960,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=10

Run status group 0 (all jobs):
   READ: bw=753MiB/s (790MB/s), 753MiB/s-753MiB/s (790MB/s-790MB/s), io=10.0GiB (10.7GB), run=13596-13596msec

Disk stats (read/write):
  vda: ios=40477/0, merge=1/0, ticks=13687/0, in_queue=13686, util=99.27%
job1: (g=0): rw=randread, bs=(R) 512KiB-512KiB, (W) 512KiB-512KiB, (T) 512KiB-512KiB, ioengine=libaio, iodepth=10
...
fio-3.32
Starting 10 threads
Jobs: 6 (f=5): [r(1),_(1),f(1),_(2),r(1),_(1),r(3)][85.7%][r=782MiB/s][r=1563 IOPS][eta 00m:02s]     
job1: (groupid=0, jobs=10): err= 0: pid=1714: Wed Apr 26 17:40:18 2023
  read: IOPS=1757, BW=879MiB/s (922MB/s)(10.0GiB/11650msec)
    slat (usec): min=259, max=49185, avg=4484.33, stdev=3874.60
    clat (usec): min=137, max=176505, avg=41683.46, stdev=20805.72
     lat (usec): min=1356, max=183727, avg=46167.79, stdev=22818.11
    clat percentiles (msec):
     |  1.00th=[    9],  5.00th=[   11], 10.00th=[   14], 20.00th=[   26],
     | 30.00th=[   31], 40.00th=[   35], 50.00th=[   41], 60.00th=[   46],
     | 70.00th=[   50], 80.00th=[   56], 90.00th=[   64], 95.00th=[   82],
     | 99.00th=[  111], 99.50th=[  120], 99.90th=[  136], 99.95th=[  144],
     | 99.99th=[  163]
   bw (  MiB/s): min=  763, max= 1946, per=100.00%, avg=1264.71, stdev=29.45, samples=184
   iops        : min= 1520, max= 3887, avg=2524.20, stdev=58.89, samples=184
  lat (usec)   : 250=0.01%, 500=0.03%, 750=0.01%
  lat (msec)   : 2=0.01%, 4=0.03%, 10=3.00%, 20=10.12%, 50=57.70%
  lat (msec)   : 100=27.20%, 250=1.89%
  cpu          : usr=1.95%, sys=86.85%, ctx=2617, majf=0, minf=3620
  IO depths    : 1=0.1%, 2=0.1%, 4=0.2%, 8=99.7%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.1%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=20480,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=10

Run status group 0 (all jobs):
   READ: bw=879MiB/s (922MB/s), 879MiB/s-879MiB/s (922MB/s-922MB/s), io=10.0GiB (10.7GB), run=11650-11650msec

Disk stats (read/write):
  vda: ios=20461/0, merge=1/0, ticks=6909/0, in_queue=6909, util=99.06%
job1: (g=0): rw=randread, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=10
...
fio-3.32
Starting 10 threads
Jobs: 7 (f=6): [r(1),_(1),r(3),f(1),r(1),_(1),r(1),_(1)][94.1%][r=698MiB/s][r=698 IOPS][eta 00m:01s]
job1: (groupid=0, jobs=10): err= 0: pid=1727: Wed Apr 26 17:41:04 2023
  read: IOPS=666, BW=667MiB/s (699MB/s)(10.0GiB/15362msec)
    slat (usec): min=447, max=72218, avg=14067.27, stdev=7315.65
    clat (usec): min=294, max=315309, avg=127492.24, stdev=45985.52
     lat (msec): min=3, max=346, avg=141.56, stdev=50.06
    clat percentiles (msec):
     |  1.00th=[   27],  5.00th=[   78], 10.00th=[   88], 20.00th=[   94],
     | 30.00th=[  103], 40.00th=[  109], 50.00th=[  114], 60.00th=[  121],
     | 70.00th=[  134], 80.00th=[  165], 90.00th=[  203], 95.00th=[  224],
     | 99.00th=[  251], 99.50th=[  264], 99.90th=[  279], 99.95th=[  300],
     | 99.99th=[  313]
   bw (  KiB/s): min=364367, max=1100963, per=100.00%, avg=705882.95, stdev=16463.04, samples=284
   iops        : min=  349, max= 1072, avg=684.21, stdev=16.18, samples=284
  lat (usec)   : 500=0.05%, 750=0.04%, 1000=0.01%
  lat (msec)   : 4=0.02%, 10=0.11%, 20=0.22%, 50=1.55%, 100=25.16%
  lat (msec)   : 250=71.73%, 500=1.11%
  cpu          : usr=0.74%, sys=80.48%, ctx=4577, majf=0, minf=1607
  IO depths    : 1=0.1%, 2=0.2%, 4=0.4%, 8=99.3%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=99.9%, 8=0.0%, 16=0.1%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=10240,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=10

Run status group 0 (all jobs):
   READ: bw=667MiB/s (699MB/s), 667MiB/s-667MiB/s (699MB/s-699MB/s), io=10.0GiB (10.7GB), run=15362-15362msec

Disk stats (read/write):
  vda: ios=10120/0, merge=0/0, ticks=4101/0, in_queue=4100, util=93.73%
job1: (g=0): rw=randwrite, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=10
...
fio-3.32
Starting 10 threads
Jobs: 10 (f=10): [w(10)][100.0%][w=46.6MiB/s][w=11.9k IOPS][eta 00m:00s]
job1: (groupid=0, jobs=10): err= 0: pid=1740: Wed Apr 26 17:42:05 2023
  write: IOPS=11.9k, BW=46.4MiB/s (48.7MB/s)(1392MiB/30005msec); 0 zone resets
    slat (usec): min=99, max=35259, avg=562.96, stdev=760.57
    clat (usec): min=81, max=127729, avg=7795.60, stdev=7454.88
     lat (usec): min=918, max=129028, avg=8358.55, stdev=7800.78
    clat percentiles (usec):
     |  1.00th=[ 4146],  5.00th=[ 4555], 10.00th=[ 4752], 20.00th=[ 5080],
     | 30.00th=[ 5276], 40.00th=[ 5538], 50.00th=[ 5735], 60.00th=[ 5997],
     | 70.00th=[ 6390], 80.00th=[ 7177], 90.00th=[11207], 95.00th=[15926],
     | 99.00th=[47973], 99.50th=[52691], 99.90th=[61080], 99.95th=[65274],
     | 99.99th=[82314]
   bw (  KiB/s): min= 7834, max=68122, per=100.00%, avg=47574.90, stdev=2058.98, samples=590
   iops        : min= 1953, max=17025, avg=11889.97, stdev=514.75, samples=590
  lat (usec)   : 100=0.01%, 250=0.01%, 500=0.01%, 750=0.01%, 1000=0.01%
  lat (msec)   : 2=0.01%, 4=0.50%, 10=86.49%, 20=8.79%, 50=3.45%
  lat (msec)   : 100=0.76%, 250=0.01%
  cpu          : usr=8.62%, sys=61.23%, ctx=293881, majf=0, minf=10
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=100.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.1%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=0,356478,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=10

Run status group 0 (all jobs):
  WRITE: bw=46.4MiB/s (48.7MB/s), 46.4MiB/s-46.4MiB/s (48.7MB/s-48.7MB/s), io=1392MiB (1460MB), run=30005-30005msec

Disk stats (read/write):
  vda: ios=0/354325, merge=0/5, ticks=0/238975, in_queue=239949, util=99.77%
job1: (g=0): rw=randwrite, bs=(R) 16.0KiB-16.0KiB, (W) 16.0KiB-16.0KiB, (T) 16.0KiB-16.0KiB, ioengine=libaio, iodepth=10
...
fio-3.32
Starting 10 threads
Jobs: 10 (f=5): [w(3),f(3),w(1),f(1),w(1),f(1)][47.7%][w=185MiB/s][w=11.9k IOPS][eta 00m:34s]
job1: (groupid=0, jobs=10): err= 0: pid=1753: Wed Apr 26 17:43:05 2023
  write: IOPS=11.3k, BW=177MiB/s (186MB/s)(5315MiB/30005msec); 0 zone resets
    slat (usec): min=104, max=69371, avg=587.73, stdev=718.57
    clat (usec): min=305, max=989889, avg=8175.14, stdev=17813.64
     lat (usec): min=865, max=990014, avg=8762.87, stdev=17935.39
    clat percentiles (msec):
     |  1.00th=[    5],  5.00th=[    5], 10.00th=[    5], 20.00th=[    6],
     | 30.00th=[    6], 40.00th=[    6], 50.00th=[    6], 60.00th=[    7],
     | 70.00th=[    7], 80.00th=[    9], 90.00th=[   12], 95.00th=[   16],
     | 99.00th=[   46], 99.50th=[   52], 99.90th=[   63], 99.95th=[   70],
     | 99.99th=[  969]
   bw (  KiB/s): min=35132, max=268290, per=100.00%, avg=184652.67, stdev=7407.01, samples=580
   iops        : min= 2191, max=16762, avg=11536.28, stdev=462.96, samples=580
  lat (usec)   : 500=0.01%, 750=0.01%, 1000=0.01%
  lat (msec)   : 2=0.01%, 4=0.28%, 10=83.48%, 20=12.68%, 50=2.97%
  lat (msec)   : 100=0.54%, 250=0.01%, 1000=0.03%
  cpu          : usr=7.88%, sys=59.67%, ctx=282282, majf=0, minf=10
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=100.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.1%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=0,340190,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=10

Run status group 0 (all jobs):
  WRITE: bw=177MiB/s (186MB/s), 177MiB/s-177MiB/s (186MB/s-186MB/s), io=5315MiB (5574MB), run=30005-30005msec

Disk stats (read/write):
  vda: ios=0/340201, merge=0/6, ticks=0/324256, in_queue=326014, util=99.58%
job1: (g=0): rw=randwrite, bs=(R) 32.0KiB-32.0KiB, (W) 32.0KiB-32.0KiB, (T) 32.0KiB-32.0KiB, ioengine=libaio, iodepth=10
...
fio-3.32
Starting 10 threads
Jobs: 2 (f=2): [_(1),w(1),_(2),w(1),_(5)][81.1%][w=150MiB/s][w=4808 IOPS][eta 00m:07s]      
job1: (groupid=0, jobs=10): err= 0: pid=1766: Wed Apr 26 17:44:06 2023
  write: IOPS=10.7k, BW=334MiB/s (350MB/s)(9.79GiB/30001msec); 0 zone resets
    slat (usec): min=111, max=25546, avg=529.00, stdev=665.58
    clat (usec): min=200, max=80269, avg=7382.16, stdev=7372.35
     lat (usec): min=473, max=83158, avg=7911.16, stdev=7692.35
    clat percentiles (usec):
     |  1.00th=[ 3490],  5.00th=[ 4080], 10.00th=[ 4490], 20.00th=[ 4948],
     | 30.00th=[ 5211], 40.00th=[ 5473], 50.00th=[ 5669], 60.00th=[ 5932],
     | 70.00th=[ 6259], 80.00th=[ 6718], 90.00th=[ 8291], 95.00th=[13829],
     | 99.00th=[47449], 99.50th=[52167], 99.90th=[60031], 99.95th=[62129],
     | 99.99th=[67634]
   bw (  KiB/s): min=95052, max=632702, per=100.00%, avg=406745.66, stdev=17742.84, samples=501
   iops        : min= 2965, max=19766, avg=12706.01, stdev=554.48, samples=501
  lat (usec)   : 250=0.01%, 500=0.01%, 750=0.01%, 1000=0.01%
  lat (msec)   : 2=0.01%, 4=4.12%, 10=87.65%, 20=4.09%, 50=3.42%
  lat (msec)   : 100=0.71%
  cpu          : usr=9.13%, sys=62.83%, ctx=280735, majf=0, minf=10
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=100.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.1%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=0,320737,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=10

Run status group 0 (all jobs):
  WRITE: bw=334MiB/s (350MB/s), 334MiB/s-334MiB/s (350MB/s-350MB/s), io=9.79GiB (10.5GB), run=30001-30001msec

Disk stats (read/write):
  vda: ios=0/319795, merge=0/7, ticks=0/200091, in_queue=201175, util=99.77%
job1: (g=0): rw=randwrite, bs=(R) 64.0KiB-64.0KiB, (W) 64.0KiB-64.0KiB, (T) 64.0KiB-64.0KiB, ioengine=libaio, iodepth=10
...
fio-3.32
Starting 10 threads
Jobs: 2 (f=2): [_(4),w(1),_(2),w(1),_(2)][94.1%][w=473MiB/s][w=7571 IOPS][eta 00m:01s]      
job1: (groupid=0, jobs=10): err= 0: pid=1779: Wed Apr 26 17:44:52 2023
  write: IOPS=10.5k, BW=659MiB/s (691MB/s)(10.0GiB/15536msec); 0 zone resets
    slat (usec): min=126, max=37466, avg=585.86, stdev=667.19
    clat (usec): min=214, max=97386, avg=7771.57, stdev=6817.27
     lat (usec): min=427, max=98821, avg=8357.42, stdev=7138.76
    clat percentiles (usec):
     |  1.00th=[ 3687],  5.00th=[ 4359], 10.00th=[ 4817], 20.00th=[ 5211],
     | 30.00th=[ 5538], 40.00th=[ 5735], 50.00th=[ 5997], 60.00th=[ 6325],
     | 70.00th=[ 6652], 80.00th=[ 7242], 90.00th=[11338], 95.00th=[15401],
     | 99.00th=[44827], 99.50th=[50070], 99.90th=[58459], 99.95th=[62129],
     | 99.99th=[80217]
   bw (  KiB/s): min=222829, max=1207995, per=100.00%, avg=762194.14, stdev=31760.89, samples=268
   iops        : min= 3477, max=18873, avg=11904.07, stdev=496.23, samples=268
  lat (usec)   : 250=0.01%, 500=0.01%, 750=0.01%, 1000=0.01%
  lat (msec)   : 2=0.01%, 4=2.48%, 10=84.96%, 20=8.58%, 50=3.43%
  lat (msec)   : 100=0.52%
  cpu          : usr=9.30%, sys=62.55%, ctx=146050, majf=0, minf=10
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=100.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.1%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=0,163840,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=10

Run status group 0 (all jobs):
  WRITE: bw=659MiB/s (691MB/s), 659MiB/s-659MiB/s (691MB/s-691MB/s), io=10.0GiB (10.7GB), run=15536-15536msec

Disk stats (read/write):
  vda: ios=0/163321, merge=0/4, ticks=0/103160, in_queue=103860, util=99.39%
job1: (g=0): rw=randwrite, bs=(R) 128KiB-128KiB, (W) 128KiB-128KiB, (T) 128KiB-128KiB, ioengine=libaio, iodepth=10
...
fio-3.32
Starting 10 threads
Jobs: 1 (f=0): [_(5),f(1),_(4)][100.0%][w=428MiB/s][w=3425 IOPS][eta 00m:00s]                         
job1: (groupid=0, jobs=10): err= 0: pid=1792: Wed Apr 26 17:45:32 2023
  write: IOPS=8313, BW=1039MiB/s (1090MB/s)(10.0GiB/9854msec); 0 zone resets
    slat (usec): min=141, max=21220, avg=731.41, stdev=616.56
    clat (usec): min=193, max=94810, avg=8824.54, stdev=5789.44
     lat (usec): min=525, max=96760, avg=9555.96, stdev=6139.46
    clat percentiles (usec):
     |  1.00th=[ 3490],  5.00th=[ 4686], 10.00th=[ 5145], 20.00th=[ 5669],
     | 30.00th=[ 6063], 40.00th=[ 6456], 50.00th=[ 6980], 60.00th=[ 7767],
     | 70.00th=[ 8717], 80.00th=[10290], 90.00th=[14615], 95.00th=[19530],
     | 99.00th=[33424], 99.50th=[39060], 99.90th=[57410], 99.95th=[60556],
     | 99.99th=[77071]
   bw (  MiB/s): min=  673, max= 2008, per=100.00%, avg=1326.83, stdev=45.78, samples=151
   iops        : min= 5383, max=16061, avg=10609.94, stdev=366.23, samples=151
  lat (usec)   : 250=0.01%, 500=0.01%, 750=0.01%, 1000=0.01%
  lat (msec)   : 2=0.02%, 4=2.31%, 10=76.24%, 20=16.80%, 50=4.35%
  lat (msec)   : 100=0.26%
  cpu          : usr=9.15%, sys=65.79%, ctx=79213, majf=0, minf=11
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=99.9%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.1%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=0,81920,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=10

Run status group 0 (all jobs):
  WRITE: bw=1039MiB/s (1090MB/s), 1039MiB/s-1039MiB/s (1090MB/s-1090MB/s), io=10.0GiB (10.7GB), run=9854-9854msec

Disk stats (read/write):
  vda: ios=0/81303, merge=0/3, ticks=0/40611, in_queue=40768, util=98.89%
job1: (g=0): rw=randwrite, bs=(R) 256KiB-256KiB, (W) 256KiB-256KiB, (T) 256KiB-256KiB, ioengine=libaio, iodepth=10
...
fio-3.32
Starting 10 threads
Jobs: 3 (f=3): [w(1),_(7),w(2)][91.7%][w=921MiB/s][w=3683 IOPS][eta 00m:01s]           
job1: (groupid=0, jobs=10): err= 0: pid=1805: Wed Apr 26 17:46:13 2023
  write: IOPS=4001, BW=1000MiB/s (1049MB/s)(10.0GiB/10236msec); 0 zone resets
    slat (usec): min=182, max=18227, avg=1832.83, stdev=1702.02
    clat (usec): min=271, max=90559, avg=18981.17, stdev=11910.57
     lat (usec): min=711, max=94292, avg=20814.00, stdev=12926.69
    clat percentiles (usec):
     |  1.00th=[ 4293],  5.00th=[ 5407], 10.00th=[ 7635], 20.00th=[10159],
     | 30.00th=[11863], 40.00th=[13698], 50.00th=[15533], 60.00th=[17957],
     | 70.00th=[22676], 80.00th=[27132], 90.00th=[31327], 95.00th=[45351],
     | 99.00th=[60556], 99.50th=[65799], 99.90th=[78119], 99.95th=[80217],
     | 99.99th=[84411]
   bw (  MiB/s): min=  621, max= 2590, per=100.00%, avg=1195.68, stdev=60.78, samples=166
   iops        : min= 2481, max=10358, avg=4778.12, stdev=243.12, samples=166
  lat (usec)   : 500=0.02%, 750=0.01%, 1000=0.01%
  lat (msec)   : 2=0.03%, 4=0.37%, 10=19.03%, 20=45.39%, 50=31.17%
  lat (msec)   : 100=3.97%
  cpu          : usr=5.68%, sys=74.18%, ctx=42415, majf=0, minf=10
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=99.8%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.1%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=0,40960,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=10

Run status group 0 (all jobs):
  WRITE: bw=1000MiB/s (1049MB/s), 1000MiB/s-1000MiB/s (1049MB/s-1049MB/s), io=10.0GiB (10.7GB), run=10236-10236msec

Disk stats (read/write):
  vda: ios=0/40659, merge=0/2, ticks=0/17536, in_queue=17748, util=98.95%
job1: (g=0): rw=randwrite, bs=(R) 512KiB-512KiB, (W) 512KiB-512KiB, (T) 512KiB-512KiB, ioengine=libaio, iodepth=10
...
fio-3.32
Starting 10 threads
Jobs: 4 (f=3): [w(1),_(1),w(1),_(1),f(1),w(1),_(4)][100.0%][w=755MiB/s][w=1509 IOPS][eta 00m:00s]
job1: (groupid=0, jobs=10): err= 0: pid=1818: Wed Apr 26 17:47:00 2023
  write: IOPS=1281, BW=641MiB/s (672MB/s)(10.0GiB/15976msec); 0 zone resets
    slat (usec): min=296, max=34600, avg=6869.97, stdev=3897.75
    clat (usec): min=236, max=191187, avg=65472.76, stdev=27070.60
     lat (usec): min=1663, max=204720, avg=72342.73, stdev=29326.57
    clat percentiles (msec):
     |  1.00th=[   16],  5.00th=[   31], 10.00th=[   37], 20.00th=[   48],
     | 30.00th=[   52], 40.00th=[   56], 50.00th=[   62], 60.00th=[   64],
     | 70.00th=[   68], 80.00th=[   81], 90.00th=[  111], 95.00th=[  126],
     | 99.00th=[  140], 99.50th=[  144], 99.90th=[  157], 99.95th=[  165],
     | 99.99th=[  182]
   bw (  KiB/s): min=422169, max=1266961, per=100.00%, avg=695339.81, stdev=20108.99, samples=291
   iops        : min=  820, max= 2469, avg=1353.80, stdev=39.23, samples=291
  lat (usec)   : 250=0.01%, 500=0.03%, 750=0.01%
  lat (msec)   : 2=0.01%, 4=0.02%, 10=0.38%, 20=0.97%, 50=23.61%
  lat (msec)   : 100=61.22%, 250=13.74%
  cpu          : usr=2.45%, sys=77.82%, ctx=23841, majf=0, minf=11
  IO depths    : 1=0.1%, 2=0.1%, 4=0.2%, 8=99.7%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.1%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=0,20480,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=10

Run status group 0 (all jobs):
  WRITE: bw=641MiB/s (672MB/s), 641MiB/s-641MiB/s (672MB/s-672MB/s), io=10.0GiB (10.7GB), run=15976-15976msec

Disk stats (read/write):
  vda: ios=0/20353, merge=0/4, ticks=0/9622, in_queue=10261, util=98.39%
job1: (g=0): rw=randwrite, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=10
...
fio-3.32
Starting 10 threads
Jobs: 9 (f=9): [w(8),_(1),w(1)][87.5%][w=655MiB/s][w=654 IOPS][eta 00m:02s]
job1: (groupid=0, jobs=10): err= 0: pid=1831: Wed Apr 26 17:47:44 2023
  write: IOPS=742, BW=743MiB/s (779MB/s)(10.0GiB/13789msec); 0 zone resets
    slat (usec): min=550, max=55579, avg=11928.05, stdev=7686.75
    clat (usec): min=340, max=311571, avg=109312.15, stdev=42576.67
     lat (msec): min=2, max=322, avg=121.24, stdev=46.22
    clat percentiles (msec):
     |  1.00th=[   24],  5.00th=[   32], 10.00th=[   39], 20.00th=[   91],
     | 30.00th=[   97], 40.00th=[  102], 50.00th=[  105], 60.00th=[  110],
     | 70.00th=[  118], 80.00th=[  133], 90.00th=[  169], 95.00th=[  192],
     | 99.00th=[  226], 99.50th=[  239], 99.90th=[  271], 99.95th=[  288],
     | 99.99th=[  300]
   bw (  KiB/s): min=532256, max=1264184, per=100.00%, avg=923544.40, stdev=16434.66, samples=241
   iops        : min=  514, max= 1230, avg=897.04, stdev=16.08, samples=241
  lat (usec)   : 500=0.04%, 750=0.04%, 1000=0.02%
  lat (msec)   : 4=0.03%, 10=0.13%, 20=0.19%, 50=10.57%, 100=26.66%
  lat (msec)   : 250=62.07%, 500=0.26%
  cpu          : usr=2.05%, sys=81.93%, ctx=13508, majf=0, minf=10
  IO depths    : 1=0.1%, 2=0.2%, 4=0.4%, 8=99.3%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=99.9%, 8=0.0%, 16=0.1%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=0,10240,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=10

Run status group 0 (all jobs):
  WRITE: bw=743MiB/s (779MB/s), 743MiB/s-743MiB/s (779MB/s-779MB/s), io=10.0GiB (10.7GB), run=13789-13789msec

Disk stats (read/write):
  vda: ios=0/10180, merge=0/2, ticks=0/6058, in_queue=6497, util=92.63%
job1: (g=0): rw=randrw, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=10
...
fio-3.32
Starting 10 threads
Jobs: 10 (f=10): [m(10)][100.0%][r=34.6MiB/s,w=14.5MiB/s][r=8862,w=3706 IOPS][eta 00m:00s]
job1: (groupid=0, jobs=10): err= 0: pid=1845: Wed Apr 26 17:48:45 2023
  read: IOPS=8957, BW=35.0MiB/s (36.7MB/s)(1050MiB/30004msec)
    slat (usec): min=98, max=52079, avg=526.15, stdev=916.16
    clat (usec): min=368, max=118510, avg=7174.41, stdev=5731.51
     lat (usec): min=680, max=118850, avg=7700.56, stdev=5994.08
    clat percentiles (usec):
     |  1.00th=[ 3785],  5.00th=[ 4178], 10.00th=[ 4359], 20.00th=[ 4686],
     | 30.00th=[ 4883], 40.00th=[ 5145], 50.00th=[ 5342], 60.00th=[ 5669],
     | 70.00th=[ 6063], 80.00th=[ 7111], 90.00th=[11731], 95.00th=[16581],
     | 99.00th=[34866], 99.50th=[39584], 99.90th=[49021], 99.95th=[54789],
     | 99.99th=[87557]
   bw (  KiB/s): min= 8567, max=51231, per=100.00%, avg=35855.24, stdev=1279.50, samples=590
   iops        : min= 2138, max=12804, avg=8959.95, stdev=319.85, samples=590
  write: IOPS=3846, BW=15.0MiB/s (15.8MB/s)(451MiB/30004msec); 0 zone resets
    slat (usec): min=100, max=82640, avg=547.06, stdev=1044.80
    clat (usec): min=84, max=111947, avg=7342.69, stdev=5670.17
     lat (usec): min=361, max=112252, avg=7889.75, stdev=5979.37
    clat percentiles (usec):
     |  1.00th=[ 3949],  5.00th=[ 4293], 10.00th=[ 4555], 20.00th=[ 4817],
     | 30.00th=[ 5080], 40.00th=[ 5276], 50.00th=[ 5538], 60.00th=[ 5866],
     | 70.00th=[ 6259], 80.00th=[ 7439], 90.00th=[11994], 95.00th=[16581],
     | 99.00th=[34341], 99.50th=[39060], 99.90th=[49546], 99.95th=[56361],
     | 99.99th=[87557]
   bw (  KiB/s): min= 3404, max=23079, per=100.00%, avg=15390.29, stdev=560.11, samples=590
   iops        : min=  848, max= 5766, avg=3844.12, stdev=139.97, samples=590
  lat (usec)   : 100=0.01%, 250=0.01%, 500=0.01%, 750=0.01%, 1000=0.01%
  lat (msec)   : 2=0.01%, 4=2.24%, 10=84.10%, 20=9.68%, 50=3.89%
  lat (msec)   : 100=0.09%, 250=0.01%
  cpu          : usr=9.33%, sys=66.47%, ctx=115700, majf=0, minf=10
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=100.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.1%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=268749,115396,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=10

Run status group 0 (all jobs):
   READ: bw=35.0MiB/s (36.7MB/s), 35.0MiB/s-35.0MiB/s (36.7MB/s-36.7MB/s), io=1050MiB (1101MB), run=30004-30004msec
  WRITE: bw=15.0MiB/s (15.8MB/s), 15.0MiB/s-15.0MiB/s (15.8MB/s-15.8MB/s), io=451MiB (473MB), run=30004-30004msec

Disk stats (read/write):
  vda: ios=266865/114580, merge=0/6, ticks=173367/76973, in_queue=250829, util=99.70%
job1: (g=0): rw=randrw, bs=(R) 16.0KiB-16.0KiB, (W) 16.0KiB-16.0KiB, (T) 16.0KiB-16.0KiB, ioengine=libaio, iodepth=10
...
fio-3.32
Starting 10 threads
Jobs: 9 (f=0): [f(3),E(1),f(6)][100.0%][r=134MiB/s,w=56.3MiB/s][r=8560,w=3604 IOPS][eta 00m:00s]
job1: (groupid=0, jobs=10): err= 0: pid=1858: Wed Apr 26 17:49:45 2023
  read: IOPS=8697, BW=136MiB/s (143MB/s)(4078MiB/30005msec)
    slat (usec): min=103, max=39754, avg=551.44, stdev=891.28
    clat (usec): min=205, max=67918, avg=7371.57, stdev=5305.41
     lat (usec): min=364, max=68727, avg=7923.02, stdev=5551.04
    clat percentiles (usec):
     |  1.00th=[ 3949],  5.00th=[ 4359], 10.00th=[ 4555], 20.00th=[ 4883],
     | 30.00th=[ 5080], 40.00th=[ 5342], 50.00th=[ 5604], 60.00th=[ 5866],
     | 70.00th=[ 6325], 80.00th=[ 7832], 90.00th=[12387], 95.00th=[16319],
     | 99.00th=[32900], 99.50th=[36439], 99.90th=[44827], 99.95th=[47973],
     | 99.99th=[54789]
   bw (  KiB/s): min=36860, max=196632, per=100.00%, avg=139239.49, stdev=4731.85, samples=590
   iops        : min= 2300, max=12284, avg=8698.03, stdev=295.75, samples=590
  write: IOPS=3735, BW=58.4MiB/s (61.2MB/s)(1751MiB/30005msec); 0 zone resets
    slat (usec): min=107, max=29270, avg=574.21, stdev=980.74
    clat (usec): min=818, max=78616, avg=7565.20, stdev=5341.55
     lat (usec): min=1050, max=78862, avg=8139.41, stdev=5632.86
    clat percentiles (usec):
     |  1.00th=[ 4080],  5.00th=[ 4490], 10.00th=[ 4686], 20.00th=[ 5014],
     | 30.00th=[ 5211], 40.00th=[ 5473], 50.00th=[ 5735], 60.00th=[ 6063],
     | 70.00th=[ 6587], 80.00th=[ 8225], 90.00th=[12649], 95.00th=[16581],
     | 99.00th=[33162], 99.50th=[36963], 99.90th=[45351], 99.95th=[49021],
     | 99.99th=[57934]
   bw (  KiB/s): min=14267, max=89181, per=100.00%, avg=59793.37, stdev=2079.24, samples=590
   iops        : min=  888, max= 5568, avg=3732.59, stdev=129.92, samples=590
  lat (usec)   : 250=0.01%, 500=0.01%, 750=0.01%, 1000=0.01%
  lat (msec)   : 2=0.01%, 4=1.08%, 10=83.33%, 20=11.89%, 50=3.65%
  lat (msec)   : 100=0.03%
  cpu          : usr=8.99%, sys=66.77%, ctx=113645, majf=0, minf=10
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=100.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.1%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=260980,112080,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=10

Run status group 0 (all jobs):
   READ: bw=136MiB/s (143MB/s), 136MiB/s-136MiB/s (143MB/s-143MB/s), io=4078MiB (4276MB), run=30005-30005msec
  WRITE: bw=58.4MiB/s (61.2MB/s), 58.4MiB/s-58.4MiB/s (61.2MB/s-61.2MB/s), io=1751MiB (1836MB), run=30005-30005msec

Disk stats (read/write):
  vda: ios=259052/111267, merge=1/5, ticks=165344/74438, in_queue=240164, util=99.79%
job1: (g=0): rw=randrw, bs=(R) 32.0KiB-32.0KiB, (W) 32.0KiB-32.0KiB, (T) 32.0KiB-32.0KiB, ioengine=libaio, iodepth=10
...
fio-3.32
Starting 10 threads
Jobs: 3 (f=3): [_(1),m(2),_(6),m(1)][96.6%][r=208MiB/s,w=88.7MiB/s][r=6659,w=2838 IOPS][eta 00m:01s]                   
job1: (groupid=0, jobs=10): err= 0: pid=1871: Wed Apr 26 17:50:43 2023
  read: IOPS=8286, BW=259MiB/s (272MB/s)(7164MiB/27668msec)
    slat (usec): min=114, max=136088, avg=557.37, stdev=976.79
    clat (usec): min=290, max=147887, avg=7361.31, stdev=5406.84
     lat (usec): min=417, max=148366, avg=7918.68, stdev=5672.03
    clat percentiles (usec):
     |  1.00th=[ 3589],  5.00th=[ 4228], 10.00th=[ 4555], 20.00th=[ 4883],
     | 30.00th=[ 5145], 40.00th=[ 5407], 50.00th=[ 5669], 60.00th=[ 5932],
     | 70.00th=[ 6390], 80.00th=[ 7635], 90.00th=[12387], 95.00th=[16057],
     | 99.00th=[33817], 99.50th=[38011], 99.90th=[47973], 99.95th=[51643],
     | 99.99th=[71828]
   bw (  KiB/s): min=68189, max=453149, per=100.00%, avg=276753.36, stdev=10001.98, samples=517
   iops        : min= 2127, max=14155, avg=8643.68, stdev=312.56, samples=517
  write: IOPS=3557, BW=111MiB/s (117MB/s)(3076MiB/27668msec); 0 zone resets
    slat (usec): min=115, max=63614, avg=584.68, stdev=1050.55
    clat (usec): min=470, max=192194, avg=7587.80, stdev=5613.51
     lat (usec): min=799, max=193468, avg=8172.47, stdev=5927.06
    clat percentiles (usec):
     |  1.00th=[ 3687],  5.00th=[ 4359], 10.00th=[ 4686], 20.00th=[ 5014],
     | 30.00th=[ 5276], 40.00th=[ 5538], 50.00th=[ 5800], 60.00th=[ 6128],
     | 70.00th=[ 6587], 80.00th=[ 7963], 90.00th=[12649], 95.00th=[16450],
     | 99.00th=[34341], 99.50th=[39060], 99.90th=[50070], 99.95th=[57934],
     | 99.99th=[79168]
   bw (  KiB/s): min=28707, max=198536, per=100.00%, avg=118900.79, stdev=4373.27, samples=517
   iops        : min=  893, max= 6199, avg=3711.16, stdev=136.69, samples=517
  lat (usec)   : 500=0.01%, 750=0.01%, 1000=0.01%
  lat (msec)   : 2=0.03%, 4=2.62%, 10=82.31%, 20=11.59%, 50=3.36%
  lat (msec)   : 100=0.07%, 250=0.01%
  cpu          : usr=9.25%, sys=67.53%, ctx=100542, majf=0, minf=10
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=100.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.1%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=229258,98422,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=10

Run status group 0 (all jobs):
   READ: bw=259MiB/s (272MB/s), 259MiB/s-259MiB/s (272MB/s-272MB/s), io=7164MiB (7512MB), run=27668-27668msec
  WRITE: bw=111MiB/s (117MB/s), 111MiB/s-111MiB/s (117MB/s-117MB/s), io=3076MiB (3225MB), run=27668-27668msec

Disk stats (read/write):
  vda: ios=228685/98217, merge=2/6, ticks=141924/66622, in_queue=209068, util=99.52%
job1: (g=0): rw=randrw, bs=(R) 64.0KiB-64.0KiB, (W) 64.0KiB-64.0KiB, (T) 64.0KiB-64.0KiB, ioengine=libaio, iodepth=10
...
fio-3.32
Starting 10 threads
Jobs: 3 (f=3): [_(1),m(1),_(3),m(1),_(3),m(1)][93.8%][r=397MiB/s,w=165MiB/s][r=6353,w=2637 IOPS][eta 00m:01s]
job1: (groupid=0, jobs=10): err= 0: pid=1884: Wed Apr 26 17:51:28 2023
  read: IOPS=7963, BW=498MiB/s (522MB/s)(7164MiB/14394msec)
    slat (usec): min=125, max=26509, avg=566.32, stdev=870.02
    clat (usec): min=162, max=65823, avg=7436.50, stdev=5440.48
     lat (usec): min=365, max=70297, avg=8002.82, stdev=5699.84
    clat percentiles (usec):
     |  1.00th=[ 3556],  5.00th=[ 4228], 10.00th=[ 4555], 20.00th=[ 4948],
     | 30.00th=[ 5211], 40.00th=[ 5473], 50.00th=[ 5735], 60.00th=[ 6063],
     | 70.00th=[ 6521], 80.00th=[ 7570], 90.00th=[12256], 95.00th=[16188],
     | 99.00th=[34866], 99.50th=[39060], 99.90th=[46400], 99.95th=[48497],
     | 99.99th=[53740]
   bw (  KiB/s): min=171438, max=865082, per=100.00%, avg=548647.23, stdev=20290.82, samples=259
   iops        : min= 2672, max=13513, avg=8567.93, stdev=317.08, samples=259
  write: IOPS=3418, BW=214MiB/s (224MB/s)(3076MiB/14394msec); 0 zone resets
    slat (usec): min=125, max=27088, avg=591.33, stdev=954.37
    clat (usec): min=314, max=67193, avg=7605.71, stdev=5462.37
     lat (usec): min=596, max=69320, avg=8197.04, stdev=5771.35
    clat percentiles (usec):
     |  1.00th=[ 3621],  5.00th=[ 4293], 10.00th=[ 4686], 20.00th=[ 5080],
     | 30.00th=[ 5407], 40.00th=[ 5669], 50.00th=[ 5932], 60.00th=[ 6259],
     | 70.00th=[ 6718], 80.00th=[ 7832], 90.00th=[12518], 95.00th=[16450],
     | 99.00th=[34866], 99.50th=[39584], 99.90th=[47449], 99.95th=[50070],
     | 99.99th=[59507]
   bw (  KiB/s): min=76483, max=367894, per=100.00%, avg=235795.33, stdev=8648.08, samples=259
   iops        : min= 1191, max= 5741, avg=3679.72, stdev=135.11, samples=259
  lat (usec)   : 250=0.01%, 500=0.01%, 750=0.01%, 1000=0.01%
  lat (msec)   : 2=0.02%, 4=3.28%, 10=82.25%, 20=10.87%, 50=3.53%
  lat (msec)   : 100=0.04%
  cpu          : usr=9.48%, sys=67.89%, ctx=50962, majf=0, minf=10
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=100.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.1%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=114627,49213,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=10

Run status group 0 (all jobs):
   READ: bw=498MiB/s (522MB/s), 498MiB/s-498MiB/s (522MB/s-522MB/s), io=7164MiB (7512MB), run=14394-14394msec
  WRITE: bw=214MiB/s (224MB/s), 214MiB/s-214MiB/s (224MB/s-224MB/s), io=3076MiB (3225MB), run=14394-14394msec

Disk stats (read/write):
  vda: ios=114572/49199, merge=1/3, ticks=68369/30997, in_queue=99641, util=99.32%
job1: (g=0): rw=randrw, bs=(R) 128KiB-128KiB, (W) 128KiB-128KiB, (T) 128KiB-128KiB, ioengine=libaio, iodepth=10
...
fio-3.32
Starting 10 threads
Jobs: 2 (f=2): [_(3),m(1),_(1),m(1),_(4)][90.0%][r=672MiB/s,w=281MiB/s][r=5372,w=2251 IOPS][eta 00m:01s]               
job1: (groupid=0, jobs=10): err= 0: pid=1897: Wed Apr 26 17:52:07 2023
  read: IOPS=6837, BW=855MiB/s (896MB/s)(7147MiB/8362msec)
    slat (usec): min=129, max=31146, avg=609.05, stdev=907.33
    clat (usec): min=152, max=70891, avg=7441.00, stdev=5869.69
     lat (usec): min=388, max=75045, avg=8050.05, stdev=6239.35
    clat percentiles (usec):
     |  1.00th=[ 2900],  5.00th=[ 3458], 10.00th=[ 3916], 20.00th=[ 4686],
     | 30.00th=[ 5080], 40.00th=[ 5407], 50.00th=[ 5669], 60.00th=[ 6063],
     | 70.00th=[ 6849], 80.00th=[ 8455], 90.00th=[12125], 95.00th=[17695],
     | 99.00th=[34341], 99.50th=[44303], 99.90th=[58983], 99.95th=[61604],
     | 99.99th=[66847]
   bw (  MiB/s): min=  556, max= 1733, per=100.00%, avg=1057.47, stdev=44.01, samples=125
   iops        : min= 4445, max=13859, avg=8455.27, stdev=352.04, samples=125
  write: IOPS=2958, BW=370MiB/s (388MB/s)(3093MiB/8362msec); 0 zone resets
    slat (usec): min=141, max=23700, avg=637.30, stdev=1024.07
    clat (usec): min=70, max=71166, avg=7681.55, stdev=6193.68
     lat (usec): min=372, max=75644, avg=8318.85, stdev=6610.17
    clat percentiles (usec):
     |  1.00th=[ 2999],  5.00th=[ 3556], 10.00th=[ 4015], 20.00th=[ 4817],
     | 30.00th=[ 5211], 40.00th=[ 5473], 50.00th=[ 5800], 60.00th=[ 6194],
     | 70.00th=[ 6980], 80.00th=[ 8717], 90.00th=[12780], 95.00th=[18744],
     | 99.00th=[36439], 99.50th=[46400], 99.90th=[60031], 99.95th=[64226],
     | 99.99th=[69731]
   bw (  KiB/s): min=242142, max=770128, per=100.00%, avg=471009.69, stdev=19251.62, samples=125
   iops        : min= 1888, max= 6011, avg=3675.01, stdev=150.41, samples=125
  lat (usec)   : 100=0.01%, 250=0.01%, 500=0.01%, 750=0.01%, 1000=0.02%
  lat (msec)   : 2=0.04%, 4=10.53%, 10=75.10%, 20=10.25%, 50=3.71%
  lat (msec)   : 100=0.33%
  cpu          : usr=8.88%, sys=70.87%, ctx=26150, majf=0, minf=12
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=99.9%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.1%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=57179,24741,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=10

Run status group 0 (all jobs):
   READ: bw=855MiB/s (896MB/s), 855MiB/s-855MiB/s (896MB/s-896MB/s), io=7147MiB (7495MB), run=8362-8362msec
  WRITE: bw=370MiB/s (388MB/s), 370MiB/s-370MiB/s (388MB/s-388MB/s), io=3093MiB (3243MB), run=8362-8362msec

Disk stats (read/write):
  vda: ios=57149/24724, merge=0/1, ticks=25807/13120, in_queue=39089, util=98.81%
job1: (g=0): rw=randrw, bs=(R) 256KiB-256KiB, (W) 256KiB-256KiB, (T) 256KiB-256KiB, ioengine=libaio, iodepth=10
...
fio-3.32
Starting 10 threads
Jobs: 3 (f=3): [_(1),m(2),_(1),m(1),_(5)][90.9%][r=671MiB/s,w=298MiB/s][r=2682,w=1192 IOPS][eta 00m:01s]
job1: (groupid=0, jobs=10): err= 0: pid=1910: Wed Apr 26 17:52:47 2023
  read: IOPS=3032, BW=758MiB/s (795MB/s)(7128MiB/9400msec)
    slat (usec): min=160, max=28718, avg=1537.58, stdev=1628.95
    clat (usec): min=152, max=93617, avg=15361.18, stdev=10429.00
     lat (usec): min=786, max=101724, avg=16898.76, stdev=11423.49
    clat percentiles (usec):
     |  1.00th=[ 4424],  5.00th=[ 4948], 10.00th=[ 5342], 20.00th=[ 7177],
     | 30.00th=[ 9634], 40.00th=[10945], 50.00th=[12256], 60.00th=[14222],
     | 70.00th=[16909], 80.00th=[22414], 90.00th=[28181], 95.00th=[33424],
     | 99.00th=[55837], 99.50th=[64750], 99.90th=[77071], 99.95th=[79168],
     | 99.99th=[90702]
   bw (  MiB/s): min=  866, max= 1905, per=100.00%, avg=1275.70, stdev=34.34, samples=133
   iops        : min= 3462, max= 7618, avg=5097.49, stdev=137.35, samples=133
  write: IOPS=1324, BW=331MiB/s (347MB/s)(3113MiB/9400msec); 0 zone resets
    slat (usec): min=213, max=27836, avg=1566.79, stdev=1663.21
    clat (usec): min=256, max=86440, avg=15438.96, stdev=10414.62
     lat (usec): min=700, max=94772, avg=17005.76, stdev=11447.44
    clat percentiles (usec):
     |  1.00th=[ 4490],  5.00th=[ 4948], 10.00th=[ 5407], 20.00th=[ 7242],
     | 30.00th=[ 9765], 40.00th=[11076], 50.00th=[12256], 60.00th=[14222],
     | 70.00th=[17171], 80.00th=[22676], 90.00th=[28181], 95.00th=[33817],
     | 99.00th=[54264], 99.50th=[62129], 99.90th=[76022], 99.95th=[80217],
     | 99.99th=[86508]
   bw (  KiB/s): min=371576, max=853484, per=100.00%, avg=570745.24, stdev=15885.86, samples=133
   iops        : min= 1445, max= 3330, avg=2224.69, stdev=62.09, samples=133
  lat (usec)   : 250=0.01%, 500=0.01%, 1000=0.01%
  lat (msec)   : 2=0.02%, 4=0.12%, 10=32.02%, 20=43.24%, 50=22.96%
  lat (msec)   : 100=1.61%
  cpu          : usr=5.00%, sys=84.69%, ctx=14192, majf=0, minf=10
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=99.8%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.1%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=28510,12450,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=10

Run status group 0 (all jobs):
   READ: bw=758MiB/s (795MB/s), 758MiB/s-758MiB/s (795MB/s-795MB/s), io=7128MiB (7474MB), run=9400-9400msec
  WRITE: bw=331MiB/s (347MB/s), 331MiB/s-331MiB/s (347MB/s-347MB/s), io=3113MiB (3264MB), run=9400-9400msec

Disk stats (read/write):
  vda: ios=28464/12442, merge=0/1, ticks=9182/4589, in_queue=13931, util=98.93%
job1: (g=0): rw=randrw, bs=(R) 512KiB-512KiB, (W) 512KiB-512KiB, (T) 512KiB-512KiB, ioengine=libaio, iodepth=10
...
fio-3.32
Starting 10 threads
Jobs: 6 (f=6): [m(1),_(1),m(1),_(1),m(3),_(1),m(1),_(1)][86.7%][r=506MiB/s,w=224MiB/s][r=1012,w=448 IOPS][eta 00m:02s]
job1: (groupid=0, jobs=10): err= 0: pid=1923: Wed Apr 26 17:53:30 2023
  read: IOPS=1132, BW=566MiB/s (594MB/s)(7127MiB/12584msec)
    slat (usec): min=268, max=35965, avg=4964.67, stdev=3656.57
    clat (usec): min=161, max=148719, avg=46328.29, stdev=21647.29
     lat (usec): min=979, max=155679, avg=51292.96, stdev=23765.47
    clat percentiles (msec):
     |  1.00th=[    9],  5.00th=[   11], 10.00th=[   18], 20.00th=[   29],
     | 30.00th=[   36], 40.00th=[   43], 50.00th=[   47], 60.00th=[   52],
     | 70.00th=[   56], 80.00th=[   59], 90.00th=[   68], 95.00th=[   89],
     | 99.00th=[  115], 99.50th=[  121], 99.90th=[  133], 99.95th=[  138],
     | 99.99th=[  146]
   bw (  KiB/s): min=485198, max=1202712, per=100.00%, avg=827532.11, stdev=16362.84, samples=203
   iops        : min=  943, max= 2344, avg=1612.02, stdev=31.93, samples=203
  write: IOPS=494, BW=247MiB/s (259MB/s)(3114MiB/12584msec); 0 zone resets
    slat (usec): min=307, max=34079, avg=5042.31, stdev=3598.07
    clat (usec): min=304, max=137301, avg=46492.50, stdev=21552.18
     lat (msec): min=2, max=156, avg=51.53, stdev=23.62
    clat percentiles (msec):
     |  1.00th=[    9],  5.00th=[   11], 10.00th=[   17], 20.00th=[   29],
     | 30.00th=[   37], 40.00th=[   44], 50.00th=[   48], 60.00th=[   52],
     | 70.00th=[   56], 80.00th=[   59], 90.00th=[   68], 95.00th=[   89],
     | 99.00th=[  115], 99.50th=[  121], 99.90th=[  131], 99.95th=[  134],
     | 99.99th=[  138]
   bw (  KiB/s): min=189332, max=535314, per=100.00%, avg=366355.58, stdev=8536.72, samples=203
   iops        : min=  362, max= 1041, avg=709.50, stdev=16.75, samples=203
  lat (usec)   : 250=0.02%, 500=0.02%
  lat (msec)   : 2=0.01%, 4=0.04%, 10=3.33%, 20=7.17%, 50=46.19%
  lat (msec)   : 100=40.13%, 250=3.08%
  cpu          : usr=2.28%, sys=86.46%, ctx=8970, majf=0, minf=11
  IO depths    : 1=0.1%, 2=0.1%, 4=0.2%, 8=99.7%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.1%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=14253,6227,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=10

Run status group 0 (all jobs):
   READ: bw=566MiB/s (594MB/s), 566MiB/s-566MiB/s (594MB/s-594MB/s), io=7127MiB (7473MB), run=12584-12584msec
  WRITE: bw=247MiB/s (259MB/s), 247MiB/s-247MiB/s (259MB/s-259MB/s), io=3114MiB (3265MB), run=12584-12584msec

Disk stats (read/write):
  vda: ios=14004/6127, merge=0/2, ticks=4955/2896, in_queue=8135, util=98.89%
job1: (g=0): rw=randrw, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=10
...
fio-3.32
Starting 10 threads
Jobs: 8 (f=7): [m(7),_(2),f(1)][88.9%][r=459MiB/s,w=215MiB/s][r=458,w=215 IOPS][eta 00m:02s] 
job1: (groupid=0, jobs=10): err= 0: pid=1936: Wed Apr 26 17:54:17 2023
  read: IOPS=453, BW=453MiB/s (475MB/s)(7096MiB/15664msec)
    slat (usec): min=378, max=56760, avg=14345.99, stdev=7480.95
    clat (usec): min=265, max=300900, avg=131626.16, stdev=45321.82
     lat (msec): min=4, max=332, avg=145.97, stdev=49.24
    clat percentiles (msec):
     |  1.00th=[   24],  5.00th=[   85], 10.00th=[   91], 20.00th=[  102],
     | 30.00th=[  111], 40.00th=[  114], 50.00th=[  120], 60.00th=[  125],
     | 70.00th=[  142], 80.00th=[  169], 90.00th=[  203], 95.00th=[  226],
     | 99.00th=[  253], 99.50th=[  262], 99.90th=[  284], 99.95th=[  288],
     | 99.99th=[  300]
   bw (  KiB/s): min=264478, max=682063, per=100.00%, avg=466871.17, stdev=10145.57, samples=292
   iops        : min=  250, max=  661, avg=449.13, stdev= 9.98, samples=292
  write: IOPS=200, BW=201MiB/s (210MB/s)(3144MiB/15664msec); 0 zone resets
    slat (usec): min=494, max=59567, avg=14773.96, stdev=7488.47
    clat (usec): min=277, max=288586, avg=132005.61, stdev=45503.98
     lat (msec): min=2, max=313, avg=146.78, stdev=49.54
    clat percentiles (msec):
     |  1.00th=[   23],  5.00th=[   86], 10.00th=[   91], 20.00th=[  101],
     | 30.00th=[  110], 40.00th=[  114], 50.00th=[  120], 60.00th=[  127],
     | 70.00th=[  140], 80.00th=[  169], 90.00th=[  203], 95.00th=[  228],
     | 99.00th=[  255], 99.50th=[  268], 99.90th=[  284], 99.95th=[  288],
     | 99.99th=[  288]
   bw (  KiB/s): min=79342, max=346788, per=100.00%, avg=207720.19, stdev=6475.51, samples=292
   iops        : min=   68, max=  331, avg=194.36, stdev= 6.37, samples=292
  lat (usec)   : 500=0.08%, 750=0.02%
  lat (msec)   : 4=0.02%, 10=0.14%, 20=0.47%, 50=2.05%, 100=16.59%
  lat (msec)   : 250=79.29%, 500=1.35%
  cpu          : usr=1.12%, sys=79.38%, ctx=7853, majf=0, minf=10
  IO depths    : 1=0.1%, 2=0.2%, 4=0.4%, 8=99.3%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=99.9%, 8=0.0%, 16=0.1%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=7096,3144,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=10

Run status group 0 (all jobs):
   READ: bw=453MiB/s (475MB/s), 453MiB/s-453MiB/s (475MB/s-475MB/s), io=7096MiB (7441MB), run=15664-15664msec
  WRITE: bw=201MiB/s (210MB/s), 201MiB/s-201MiB/s (210MB/s-210MB/s), io=3144MiB (3297MB), run=15664-15664msec

Disk stats (read/write):
  vda: ios=6964/3098, merge=0/3, ticks=2949/1887, in_queue=5187, util=92.67%
```