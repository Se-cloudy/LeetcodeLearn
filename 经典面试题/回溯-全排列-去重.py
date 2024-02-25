"""
47. 全排列 II
中等
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

示例 1：
输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]

 zzl：从全排列改，直接学习。
 https://leetcode.cn/problems/permutations/solutions/9914/hui-su-suan-fa-python-dai-ma-java-dai-ma-by-liweiw/?envType=study-plan-v2&envId=top-100-liked
"""
from typing import List


def func(nums: List[int]) -> List[List[int]]:
    res = []
    n = len(nums)
    path = [0] * n  # 存一个path即可
    visited = [False] * n  # 回溯必备

    def dfs(i: int):
        if i == n:
            res.append(path.copy())
            return  # 回溯到上一层
        for j in range(n):  # 遍历visited
            if not visited[j]:
                if j > 0 and nums[j] == nums[j - 1] and not visited[j - 1]:
                    # 去除重复。当前值和上一个值分明一样，visited却是false，说明被手动复位过了，应该剪枝
                    continue
                path[i] = nums[j]
                visited[j] = True
                dfs(i + 1)
                visited[j] = False  # 恢复现场
                # 注意 path 无需恢复现场，因为排列长度固定，直接覆盖就行

    dfs(0)
    return res


if __name__ == "__main__":
    x = [1, 1, 3]
    prt = func(x)
    print(prt)
