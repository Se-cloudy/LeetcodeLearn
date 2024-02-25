"""
1. 两数之和 简单
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。

示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

这都背不下来我真是nt。。要注意答案有且唯一 很强很强的约束
"""
from typing import List


def fun1(nums: List[int], target: int) -> List[int]:
    res = []
    dic = {}
    # 另。可以用enumerate遍历, for i,x in ..., x = nums[i]
    for i in range(len(nums)):
        temp = target - nums[i]
        if temp in dic:
            res = [dic[temp], i]
            return res
        dic[nums[i]] = i
    return res


if __name__ == "__main__":
    x = [2,7,11,15]
    y = 9
    prt = fun1(x, y)
    print(prt)
