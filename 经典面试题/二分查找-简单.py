"""
35. 搜索插入位置 简单
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
请必须使用时间复杂度为 O(log n) 的算法。

示例 1:
输入: nums = [1,3,5,6], target = 5
输出: 2

zzl: 二分查找必须背清楚。查找比排序简单多了啊，我都一次写出来了？ok，目标不存在的时候要返回需要插入的位置。这数组都有序的。。
硬打补丁感觉好丑。。还错了。。看答案吧
tmd我2021年九月的提交用C++击败了100%的时间复杂度。。什么退步。。
注意rl加减 while取等。
"""
from typing import List


def func(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


if __name__ == "__main__":
    x = [1, 3, 5, 6]
    y = 4
    prt = func(x, y)
    print(prt)
