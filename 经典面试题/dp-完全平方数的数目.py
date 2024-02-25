"""
279. 完全平方数 中等
给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。
完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。

示例 1：
输入：n = 12
输出：3
解释：12 = 4 + 4 + 4

示例 2：
输入：n = 13
输出：2
解释：13 = 4 + 9

1 <= n <= 10^4

zzl: 依稀也做过。。不太会。最大不过100^2。。不会，学学。确实学过，精妙简洁的遍历
只得到结果不得到路径，就是dp.就算我觉得n还挺大的。。
注意各种+1取整的细节。
"""
import collections
from typing import List

import numpy as np


def func(n: int) -> int:
    dp = [0] * (n+1)
    for i in range(1,n+1):
        dp[i] = min(dp[i-j**2]+1 for j in range(1, int(i**0.5)+1))
    return dp[n]


if __name__ == "__main__":
    x = 13
    y = 2
    prt = func(x)
    print(prt)
