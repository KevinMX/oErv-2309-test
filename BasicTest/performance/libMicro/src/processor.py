import re
import sys
import os
fin = open(sys.argv[1], encoding='UTF-8')
fout= open(os.path.splitext(os.path.split(sys.argv[1])[1])[0]+".csv",'w')
startline=re.compile(r"             prc thr   usecs/call      samples   errors cnt/samp ")
resline=re.compile(r"(\w+)\s+\d+\s+\d+\s+([\d.]+)\s+\d+\s+\d+\s+\d+")
fout.write("测试类型,测试结果\n")
line = fin.readline()
while line:
    matchObj = startline.match(line)
    if matchObj:
        # print("success")
        # fout.writelines([matchObj.group(1),",",matchObj.group(2),","])
        line = fin.readline()
        matchObj = resline.match(line)
        if matchObj:
            fout.writelines([matchObj.group(1),",",matchObj.group(2),"\n"])
    line = fin.readline()
fin.close()
fout.close()