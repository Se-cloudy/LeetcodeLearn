'''
56. 合并区间 中等
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，
该数组需恰好覆盖输入中的所有区间 。

示例 1：

输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
'''
from typing import List

# 先自己写通了然后看了参考默写复现的
intervals = [[1,4],[2,3],[8,10],[9,18]]
intervals.sort()
res = [intervals[0]]
for i in intervals[:]:
    if i[0] > res[-1][1]:
        res.append(i)
    elif i[1] > res[-1][1]:
        res[-1][1] = i[1]
print(res)

"""
2024.1.5
zzl：做过的，再试试。16.22-16.27初步AC；各种乱序情况。。16.30AC
——我期待烟花漫天，能够靠在你左肩。
"""
def func(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    res = [intervals[0]]
    for i, cur in enumerate(intervals[1:]):
        if cur[0] <= res[-1][1]:
            if cur[1] > res[-1][1]:
                res[-1][1] = cur[1]
        else:
            res.append(cur)
    return res


if __name__ == "__main__":
    x = [[1,4],[0,4]]
    prt = func(x)
    print(prt)
