import re
import sys
import os
fin = open(sys.argv[1], encoding='UTF-8')
fout= open(os.path.splitext(os.path.split(sys.argv[1])[1])[0]+".csv",'w')
line = fin.readline()
startline=re.compile(r"MIGRATED (.+) TEST from 0.0.0.0 \(0.0.0.0\) port 0 AF_INET to 10.0.2.17 \(\) port 0 AF_INET")
resline=re.compile(r"\d+\s+\d+\s+[\d.]*\s+[\d.]*\s+[\d.]*\s+([\d.]*)\s+([\d.]*)")
fout.write("测试项目,测试结果\n")
while line:
    matchObj = startline.match(line)
    if matchObj:
        # print("success")
        fout.write(matchObj.group(1))
        count=0
        while resline.match(line)==None and count<=10:
            line = fin.readline()
            count+=1
        matchObj = resline.match(line)
        if matchObj:
            if matchObj.group(2)=="":
                fout.writelines([",",matchObj.group(1)])
            else:
                fout.writelines([",",matchObj.group(2)])
        fout.write("\n")
    line = fin.readline()
fin.close()
fout.close()