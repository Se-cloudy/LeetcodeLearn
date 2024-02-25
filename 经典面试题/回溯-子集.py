"""
78. 子集 中等
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

示例 1：
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

zzl：还是不会写 。。 还有人用位运算的。。 也用不来。。
逐步调试，精妙。学习吧。
"""
from typing import List


def func(nums: List[int]) -> List[List[int]]:
    res = []
    path = []
    n = len(nums)

    def dfs(i):
        if i == n:  # 为什么是这样跳出；总的跳出；
            res.append(path[:])  # 或者path.copy()，不能是path
            return
        # 不选 i
        dfs(i+1)
        # 选 i
        path.append(nums[i])
        dfs(i+1)
        path.pop()  # todo 恢复现场 还是不懂
    dfs(0)
    return res


if __name__ == "__main__":
    x = [1,2,3]
    prt = func(x)
    print(prt)
