# 9.30 19.06
# 2136. 全部开花的最早一天
# 直接看题解。贪心思路。
# 19.25 AC

plantTime = [1,4,3]
growTime = [2,3,1]
# 输出：9
res1 = 0
res2 = 0
ls = zip(growTime, range(len(growTime)))
for val, index in sorted(ls, reverse=True):  #gtime 升序排列，index是对应花的下标
    ctime = plantTime[index]
    res1 += ctime  #种花时间
    res2 = max(res2, res1 + growTime[index])  # 看的答案。
print(res2)
