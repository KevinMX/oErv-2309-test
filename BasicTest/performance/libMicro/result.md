# libMicro 测试报告

## 概述

libMicro 可用于衡量各自系统调用和 lib 库调用的性能，选择了 259 个常用的系统调用来评测操作系统系统调用方面的性能。

## 测试环境

- 发行版版本：openEuler 23.03 RISC-V Preview V1
- 内核版本：6.1.19
- 虚拟机版本：QEMU 8.0.2

## 测试方法

见 [method.md](./method.md)

## 测试结果

测试通过，测试结果详见 [log](./log) 目录下的日志文件。

### QEMU 测试结果

| 测试类型           | 测试结果       |
|----------------|------------|
| getpid         | 0.67073    |
| getenv         | 0.37343    |
| getenvT2       | 0.46494    |
| gettimeofday   | 0.14568    |
| log            | 0.11214    |
| exp            | 0.10909    |
| lrand48        | 0.08267    |
| memset_10      | 0.0344     |
| memset_256     | 0.0596     |
| memset_256_u   | 0.08256    |
| memset_1k      | 0.17467    |
| memset_4k      | 0.62755    |
| memset_4k_uc   | 0.64496    |
| memset_10k     | 1.52392    |
| memset_1m      | 216.1712   |
| memset_10m     | 2122.4781  |
| memsetP2_10m   | 1809.3656  |
| memrand        | 0.04708    |
| isatty_yes     | 14.60078   |
| isatty_no      | 0.88149    |
| malloc_10      | 0.16545    |
| malloc_100     | 0.16314    |
| malloc_1k      | 0.19309    |
| malloc_10k     | 0.42279    |
| malloc_100k    | 50.36765   |
| mallocT2_10    | 0.19258    |
| mallocT2_100   | 0.29533    |
| mallocT2_1k    | 0.24117    |
| mallocT2_10k   | 0.42774    |
| mallocT2_100k  | 116.02743  |
| close_bad      | 0.83432    |
| close_tmp      | 3.4937     |
| close_usr      | 3.61695    |
| close_zero     | 3.65453    |
| memcpy_10      | 0.06905    |
| memcpy_1k      | 0.29666    |
| memcpy_10k     | 2.24735    |
| memcpy_1m      | 340.257    |
| memcpy_10m     | 3463.779   |
| strcpy_10      | 0.10979    |
| strcpy_1k      | 0.52546    |
| strlen_10      | 0.03598    |
| strlen_1k      | 0.22201    |
| strchr_10      | 0.03514    |
| strchr_1k      | 0.24746    |
| strcmp_10      | 0.05169    |
| strcmp_1k      | 1.95037    |
| scasecmp_10    | 0.08753    |
| scasecmp_1k    | 4.03543    |
| strtol         | 0.06781    |
| getcontext     | 7.23285    |
| setcontext     | 7.44894    |
| mutex_st       | 0.09808    |
| mutex_mt       | 0.1073     |
| mutex_T2       | 0.46267    |
| longjmp        | 0.07944    |
| siglongjmp     | 8.8504     |
| getrusage      | 15.61567   |
| times          | 13.99382   |
| time           | 0.09088    |
| localtime_r    | 0.60086    |
| strftime       | 2.16471    |
| mktime         | 54.85351   |
| mktimeT2       | 181.71974  |
| c_mutex_1      | 0.32444    |
| c_mutex_10     | 834.5394   |
| c_mutex_200    | 29593.3885 |
| c_cond_1       | 0.54692    |
| c_cond_10      | 882.52482  |
| c_cond_200     | 31148.46   |
| c_lockf_1      | 80.62813   |
| c_lockf_10     | 2464.268   |
| c_lockf_200    | 55704.329  |
| c_flock        | 10.14958   |
| c_flock_10     | 38.16631   |
| c_flock_200    | 8421.7995  |
| c_fcntl_1      | 83.97908   |
| c_fcntl_10     | 1983.666   |
| c_fcntl_200    | 64221.8295 |
| file_lock      | 41.61326   |
| getsockname    | 20.30389   |
| getpeername    | 20.08867   |
| chdir_tmp      | 145.64949  |
| chdir_usr      | 159.03835  |
| chgetwd_tmp    | 159.14785  |
| chgetwd_usr    | 172.36297  |
| realpath_tmp   | 419.14488  |
| realpath_usr   | 459.71718  |
| stat_tmp       | 101.05903  |
| stat_usr       | 113.61963  |
| fcntl_tmp      | 0.8907     |
| fcntl_usr      | 0.88891    |
| fcntl_ndelay   | 0.97494    |
| lseek_t8k      | 0.79785    |
| lseek_u8k      | 0.80246    |
| open_tmp       | 113.85532  |
| open_usr       | 126.38236  |
| open_zero      | 70.51538   |
| dup            | 1.24409    |
| socket_u       | 16.64439   |
| socket_i       | 18.14846   |
| socketpair     | 77.09223   |
| setsockopt     | 13.93984   |
| bind           | 31.39889   |
| listen         | 1.5198     |
| connection     | 310.57028  |
| poll_10        | 49.72951   |
| poll_100       | 363.08824  |
| poll_1000      | 3778.33285 |
| poll_w10       | 49.53175   |
| poll_w100      | 358.89344  |
| poll_w1000     | 3790.969   |
| select_10      | 27.38444   |
| select_100     | 55.82885   |
| select_1000    | 346.67435  |
| select_w10     | 36.39447   |
| select_w100    | 65.47642   |
| select_w1000   | 358.162    |
| semop          | 26.81363   |
| sigaction      | 15.66602   |
| signal         | 106.37982  |
| sigprocmask    | 14.86985   |
| pthread_16     | 347.12631  |
| pthread_32     | 364.96253  |
| pthread_128    | 365.61662  |
| pthread_512    | 365.24367  |
| fork_10        | 634.9897   |
| fork_100       | 598.31896  |
| fork_1000      | 1059.40566 |
| exit_10        | 317.602    |
| exit_100       | 194.27663  |
| exit_1000      | 745.42294  |
| exit_10_nolibc | 242.5963   |
| exec           | 5652.1767  |
| system         | 44190.815  |
| recurse        | 2.03268    |
| read_t1k       | 16.51213   |
| read_t10k      | 40.72991   |
| read_t100k     | 297.2339   |
| read_u1k       | 16.5178    |
| read_u10k      | 33.61815   |
| read_u100k     | 218.74195  |
| read_z1k       | 12.05136   |
| read_z10k      | 24.46379   |
| read_z100k     | 162.89527  |
| read_zw100k    | 167.17023  |
| write_t1k      | 28.17841   |
| write_t10k     | 75.6695    |
| write_t100k    | 592.265    |
| write_u1k      | 31.24399   |
| write_u10k     | 82.76836   |
| write_u100k    | 644.8988   |
| write_n1k      | 0.96981    |
| write_n10k     | 0.98492    |
| write_n100k    | 0.98181    |
| writev_t1k     | 146.01389  |
| writev_t10k    | 662.9954   |
| writev_t100k   | 5751.844   |
| writev_u1k     | 153.64695  |
| writev_u10k    | 711.5762   |
| writev_u100k   | 6311.004   |
| writev_n1k     | 15.73667   |
| writev_n10k    | 15.60274   |
| writev_n100k   | 15.81987   |
| pread_t1k      | 16.68011   |
| pread_t10k     | 39.74444   |
| pread_t100k    | 296.93755  |
| pread_u1k      | 16.25066   |
| pread_u10k     | 32.8888    |
| pread_u100k    | 218.69105  |
| pread_z1k      | 11.94098   |
| pread_z10k     | 25.03351   |
| pread_z100k    | 165.97596  |
| pread_zw100k   | 171.72063  |
| pwrite_t1k     | 28.02989   |
| pwrite_t10k    | 76.34017   |
| pwrite_t100k   | 583.0682   |
| pwrite_u1k     | 31.16967   |
| pwrite_u10k    | 81.99788   |
| pwrite_u100k   | 645.5872   |
| pwrite_n1k     | 0.94781    |
| pwrite_n10k    | 0.94576    |
| pwrite_n100k   | 0.94766    |
| mmap_z8k       | 11.95771   |
| mmap_z128k     | 11.91229   |
| mmap_t8k       | 12.71108   |
| mmap_t128k     | 12.80791   |
| mmap_u8k       | 12.84026   |
| mmap_u128k     | 12.47335   |
| mmap_a8k       | 6.57173    |
| mmap_a128k     | 6.56148    |
| mmap_rz8k      | 61.37702   |
| mmap_rz128k    | 469.77629  |
| mmap_rt8k      | 61.99838   |
| mmap_rt128k    | 266.7872   |
| mmap_ru8k      | 61.56851   |
| mmap_ru128k    | 282.0966   |
| mmap_ra8k      | 48.72884   |
| mmap_ra128k    | 439.5956   |
| mmap_wz8k      | 104.79791  |
| mmap_wz128k    | 941.96425  |
| mmap_wt8k      | 118.02371  |
| mmap_wt128k    | 1081.49375 |
| mmap_wu8k      | 112.31151  |
| mmap_wu128k    | 1073.22637 |
| mmap_wa8k      | 80.7693    |
| mmap_wa128k    | 883.1145   |
| unmap_z8k      | 13.97458   |
| unmap_z128k    | 13.51706   |
| unmap_t8k      | 13.70967   |
| unmap_t128k    | 13.57467   |
| unmap_u8k      | 13.94956   |
| unmap_u128k    | 13.50678   |
| unmap_a8k      | 22.53939   |
| unmap_a128k    | 22.74451   |
| unmap_rz8k     | 41.89202   |
| unmap_rz128k   | 47.51404   |
| unmap_rt8k     | 49.42864   |
| unmap_rt128k   | 84.78311   |
| unmap_ru8k     | 47.99408   |
| unmap_ru128k   | 85.81497   |
| unmap_ra8k     | 54.31694   |
| unmap_ra128k   | 58.42469   |
| conn_connect   | 93.10533   |
| unmap_wz8k     | 69.19459   |
| unmap_wz128k   | 163.47196  |
| unmap_wt8k     | 69.40855   |
| unmap_wt128k   | 154.3338   |
| unmap_wu8k     | 68.87259   |
| unmap_wu128k   | 165.99485  |
| unmap_wa8k     | 83.13392   |
| unmap_wa128k   | 184.49125  |
| mprot_z8k      | 12.79491   |
| mprot_z128k    | 11.90954   |
| mprot_wz8k     | 41.43372   |
| mprot_wz128k   | 41.53393   |
| mprot_twz8k    | 43.13524   |
| mprot_tw128k   | 42.61739   |
| mprot_tw4m     | 149.7892   |
| pipe_pst1      | 33.315     |
| pipe_pmt1      | 201.71956  |
| pipe_pmp1      | 199.81492  |
| pipe_pst4k     | 35.22354   |
| pipe_pmt4k     | 205.6927   |
| pipe_pmp4k     | 203.5169   |
| pipe_sst1      | 53.52482   |
| pipe_smt1      | 288.99442  |
| pipe_smp1      | 287.21742  |
| pipe_sst4k     | 73.29448   |
| pipe_smt4k     | 352.69816  |
| pipe_smp4k     | 350.05626  |
| pipe_tst1      | 139.08884  |
| pipe_tmt1      | 376.81752  |
| pipe_tmp1      | 373.9358   |
| pipe_tst4k     | 118.83441  |
| pipe_tmt4k     | 386.33556  |
| pipe_tmp4k     | 380.96058  |
| conn_accept    | 63.98824   |
| close_tcp      | 45.1465    |
