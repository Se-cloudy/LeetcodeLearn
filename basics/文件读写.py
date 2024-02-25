#2023.9.13.14:29
#delta>=3
#实现list遍历 14:49
#封装函数; 类的实例调用；14:57
#测试用例报错;够不着.看题解 重新模拟；15:11;
#range小bug;
# AC: 15:22

from typing import List
data = [["一宵", "宫灯", "明"],["霓裳", "素雨", "停"]]
f = open("../data.csv", "r")
cur = []
for i in f:
    cur.append(i.strip("\n").split(","))
f.close()
for row in cur:
    line = ""
    for item in row:
        line += "{}\t".format(item)
    print(line)

