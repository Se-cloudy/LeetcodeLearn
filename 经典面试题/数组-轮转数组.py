"""
189. 轮转数组 中等
给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。

示例 1:
输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]

zzl:  五分钟，模拟。哦，要原地修改。。二十分钟。还有特例。
参考答案，
"""
import collections
from typing import List

import numpy as np


def rotate(self, nums: List[int], k: int) -> None:
    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k]

def func(nums: List[int], k: int) -> None:
    n = len(nums)
    if n < k:
        k = k % n
    temp = nums[n-k:]
    for i in range(n-1, k-1, -1):  # start, end, step 左闭右开，end要多取一位
        nums[i] = nums[i-k]
    for i in range(k):
        nums[i] = temp[i]


if __name__ == "__main__":
    x = [-1]
    y = 2
    func(x, y)
    print(x)
