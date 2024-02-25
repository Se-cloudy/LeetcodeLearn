"""
416. 分割等和子集 中等
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

示例 1：
输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。

zzl 会写回溯 看懂dp
"""
import collections
from typing import List
import numpy as np


def func(nums: List[int]) -> bool:
    n = len(nums)
    total = sum(nums)
    maxNum = max(nums)
    target = total // 2  # 问题等价于找到一个子数组和为target 感觉可以用回溯！绝对可以吧！！

    # 各种特殊
    if n < 2 or total % 2 == 1 or maxNum > target:
        return False

    dp = [[0] * (target + 1) for _ in range(n)]
    for i in range(n):
        dp[i][0] = 1
    dp[0][nums[0]] = 1  # budong

    for i in range(1,n):
        for j in range(1,target + 1):
            dp[i][j] = dp[i-1][j]  # 先继承上一个的
            if j > nums[i]:  # 和大于当前值。有可能加入当前值进行构造
                dp[i][j] = dp[i][j] or dp[i-1][j - nums[i]]
    return True if dp[n - 1][target] else False


def func2(ls) -> bool:
    # 回溯 找到和为target的子集
    res = False
    n = len(ls)
    target = sum(ls) // 2
    path = []

    def dfs(begin):
        nonlocal res
        if sum(path) == target:
            res = True
            return  # 这里要怎么才能直接返回 输出True 而不是只返回到上一级继续dfs。不要继续dfs了。 需要用nonlocal 声明
        if sum(path) > target:
            return
        for i in range(begin, n):
            path.append(ls[i])
            dfs(i + 1)
            path.pop()
            if res:
                return

    dfs(0)
    return res


if __name__ == '__main__':
    array = [10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21]
    print(func([1, 5, 11, 5]))
