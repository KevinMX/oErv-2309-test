import re
import sys
import os
fin = open(sys.argv[1], encoding='UTF-8')
fout= open(os.path.splitext(os.path.split(sys.argv[1])[1])[0]+".csv",'w')
line = fin.readline()
startline=re.compile(r"job1: \(g=0\): rw=(\w*), bs=\(R\) ([\d.]*\w*B)-\2, \(W\) \2-\2, \(T\) \2-\2, ioengine=libaio, iodepth=10")
resline=re.compile(r"Jobs: \d* \(f=\d*\): \[\S*?\]\[[\d.]*%\]\[([\s\S]*)\]\[eta \d{2}m:\d{2}s\]")
fout.write("测试类型,块大小,测试结果\n")
while line:
    matchObj = startline.match(line)
    if matchObj:
        # print("success")
        fout.writelines([matchObj.group(1),",",matchObj.group(2),","])
        count=0
        while resline.match(line)==None and count<=5:
            line = fin.readline()
            count+=1
        matchObj = resline.match(line)
        if matchObj:
            fout.writelines(["\"[",matchObj.group(1),"]\""])
        fout.write("\n")
    line = fin.readline()
fin.close()
fout.close()