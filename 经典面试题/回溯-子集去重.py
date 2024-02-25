"""
90. 子集 II 中等
给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。

示例 1：
输入：nums = [1,2,2]
输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]

zzl: 继续抄。。子集还得用标准回溯不然我改不来去重。
隔几天又不会了 为什么是begin。。。
"""
from typing import List


def func(nums: List[int]) -> List[List[int]]:
    res = []
    path = []
    n = len(nums)

    def dfs(begin):
        res.append(path[:])  # 没有输出条件
        for i in range(begin, n): # 后续元素
            if i > begin and nums[i] == nums[i-1]:  # 这个倒是背熟了
                continue
            path.append(nums[i])  # 选
            dfs(i+1)  # 不选i
            path.pop()  # 清理分支
    dfs(0)
    return res


if __name__ == "__main__":
    x = [1,2,2]
    prt = func(x)
    print(prt)
