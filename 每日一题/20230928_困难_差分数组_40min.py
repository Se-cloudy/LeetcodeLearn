# 9.28,20:42
# 节日独处啊 hard 还是花花 今天才去了植物园。
# 2251. 花期内花的数目
# 20.51写好了模拟 超出内存限制xs我觉得我dict肯定没错 就是循环有点多。
# 评论 差分数组。看答案。差分数组记录每个节点花的数量变化，最后累加得到当前数目。
# 抄了 看懂了 为什么复制的就是对的 我的就是错的。
# 21:30 抄的AC
from collections import Counter

flowers = [[19,37],[19,38],[19,35]]
people = [6,7,21,1,13,37,5,37,46,43]
# 输出：[2,2,1]
diff = Counter()
res = []
for start,end in flowers:
    diff[start] += 1
    diff[end] -= 1
times = sorted(diff.keys()) # 保证时间段和人对应

curnuum = 0
curtime = 0

for p, i in sorted(zip(people, range(len(people)))):
    while curtime<len(times) and times[curtime]<=p:
        curnuum += diff[times[curtime]]
        curtime += 1
    people[i] = curnuum

print(people)