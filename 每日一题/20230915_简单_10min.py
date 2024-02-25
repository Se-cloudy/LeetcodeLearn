#2023.9.15:14:00
# #LCP 50. 宝石补给

#14:05 居然没通过。。估计def封装有问题
#笑死。。我把初值写死进去了 def没问题。但是测试还是出错，向下取整的问题。
#14:10AC

from typing import List

def renew(cur: List[int],op:List[int])->List[int]:
    x = op[0]
    y = op[1]
    cur[y] += cur[x]//2
    cur[x] -= cur[x]//2


gem = [0,2,5,4]
operations = [[3,2],[3,2],[1,3],[0,2],[3,0],[3,1],[0,3],[2,1],[3,0]]
for i in operations:
    #renew(gem,i)
    x = i[0]
    y = i[1]
    gem[y] += gem[x]//2
    gem[x] -= gem[x]//2
    print ("via {} to {}".format(i,gem))

res = max(gem)-min(gem)
print(res)
