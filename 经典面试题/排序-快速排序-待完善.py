"""
快速排序
还要学降序和partition函数写法
partition的思想应用 求第k个最大数值
"""
import collections
from typing import List
import numpy as np


def func(nums: List[int], start, end):
    # 升序快排
    if start >= end:
        return
    left = start  # 游标，不能直接用start
    right = end
    pivot = nums[start]
    while left < right:
        while left < right and pivot <= nums[right]:
            right -= 1
        nums[left] = nums[right]

        while left < right and pivot > nums[left]:
            left += 1
        nums[right] = nums[left]
    # left是应该放入pivot的下标，退出while时l=r，下面三行用left/right都一样
    nums[left] = pivot
    func(nums, start, left - 1)
    func(nums, left + 1, end)  # 写对边界求求了


class Solution:  # 快速排序思想应用
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 找到数组中第k大的值
        def quickSelect(left, right, k):
            # you can call random here
            i, j = left, right
            while i < j:
                while nums[j] >= nums[left] and i < j:
                    j -= 1
                while nums[i] <= nums[left] and i < j:
                    i += 1
                nums[i], nums[j] = nums[j], nums[i]
            nums[i], nums[left] = nums[left], nums[i]
            if i == right + 1 - k:
                return nums[i]
            elif i < right + 1 - k:
                return quickSelect(i + 1, right, k)
            else:
                return quickSelect(left, i - 1, k - (right - i + 1))  # 细节关键

        n = len(nums)
        left, right = 0, n - 1
        return quickSelect(left, right, k)


if __name__ == "__main__":
    x = [1, 4, 2, 3]
    y = 11
    func(x, 0, len(x) - 1)
    print(x)
