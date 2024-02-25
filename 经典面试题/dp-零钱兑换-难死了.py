"""
322. 零钱兑换 中等
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
你可以认为每种硬币的数量是无限的。

示例 1：
输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1

zzl: 我今天就要把dp刷会。。感觉这个可以用回溯的思路做。。清晰点。。
这都dfs了明明是回溯。。直接学习。诶，改了改我的又感觉能用了。。就差一点。这dp怎么是二维啊。。完全不会，一个小时了。。今天学会这两种方法就差不多了吧。。呜呜
还是学吧。背包问题。标准解法就是DP。而且是二维dp[][]
"""
import collections
from typing import List
import numpy as np


def func(coins: List[int], amount: int) -> int:
    # 伟大的dfs 伟大的回溯 没有遍历amount了
    n = len(coins)

    def dfs(i, j):
        if i < 0:
            return 0 if j == 0 else np.inf
        if j < coins[i]:
            return dfs(i-1, j)
        return min(dfs(i-1, j), dfs(i, j - coins[i]) + 1)
    res = dfs(n-1, amount)  # coins 的下标从0到n-1
    return res if res < np.inf else -1

def func1(coins: List[int], amount: int) -> int:
    # dp 背包标答 细节逼死人了
    n = len(coins)
    dp = [[np.inf] * (amount + 1) for _ in range(n+1)]  # 需要取不可能达到的最大值。在min的时候就不会取到了。
    dp[0][0] = 0
    for i in range(n):  # 遍历硬币
        for j in range(amount+1):  # 遍历数值（背包）
            if j < coins[i]:  # 不放入
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = min(dp[i][j], dp[i+1][j-coins[i]]+1)  # 这里也是i-1 很烦
    res = dp[n][amount]
    return res if res < np.inf else -1


if __name__ == "__main__":
    x = [1, 2, 5]
    y = 11
    prt = func(x,y)
    print(prt)
