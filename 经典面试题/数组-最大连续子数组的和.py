"""
53. 最大子数组和 中等
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
子数组 是数组中的一个连续部分。

示例 1：
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

zzl: 15:13,15：25，有很多逻辑可以优化。果然超时了md分析下复杂度。他要求On甚至分治md。用了前缀和了，再用dp优化？
15.35看答案 真是dp dp我的神我对不起你我不够熟练呜呜 dp 贪心 两大真神啊，前缀和改改也可以做 呜呜 我是废物
——只返回结果，不求具体子序列，用dp
——返回所有结果，回溯

2024.1.8百度一面的题
"""
import collections
from typing import List

import numpy as np


def func0(nums: List[int]) -> int:
    res = -np.Inf
    # 用前缀和试试
    n = len(nums)
    pre = [0] * n
    pre[0] = nums[0]
    for i in range(1, n):
        pre[i] = pre[i-1] + nums[i]
    # 用dp优化时间吧。不行。要连续。看答案吧。
    f = [0] * n
    for i in range(n):
        if nums[i] > 0:
            f[i] += f[i-1]

    for i in range(n):
        cur = pre[i]
        for j in range(i):
            if pre[j] < 0:
                cur = max(cur, pre[i] - pre[j])
        res = max(cur, res)
    return res

def func1(nums:List[int]) -> int:
    # 前缀和改版 贪心
    res = nums[0]
    n = len(nums)
    pre = nums[0]
    for i in range(1, n):
        pre = max(pre + nums[i], nums[i])  # 断或者不断的选择 精妙
        res = max(res, pre)
    return res

def func2(nums:List[int]) -> int:
    # dp 本质与func1一样
    n = len(nums)
    dp = [0] * n

    dp[0] = nums[0]
    for i in range(1, n):
        if dp[i-1] < 0:
            dp[i] = nums[i]
        else:
            dp[i] = dp[i-1] + nums[i]
    return max(dp)


if __name__ == "__main__":
    x = [-2,1,-3,4,-1,2,1,-5,4]
    y = "aab"
    prt = func2(x)
    print(prt)
