"""
46. 全排列
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

示例 1：
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
示例 2：

输入：nums = [0,1]
输出：[[0,1],[1,0]]

zzl: 回溯，dfs，直接学习。不理解但是背下来吧。
"""
from typing import List

def func(nums: List[int]) -> List[List[int]]:
    res = []
    n = len(nums)
    path = [0] * n  # 存一个path即可
    visited = [False] * n  # 回溯必备

    def dfs(i: int) -> None:
        if i == n:
            res.append(path.copy())
            return
        for j in range(n):  # 遍历visited
            if not visited[j]:
                path[i] = nums[j]
                visited[j] = True
                dfs(i + 1)
                visited[j] = False  # 恢复现场
                # 注意 path 无需恢复现场，因为排列长度固定，直接覆盖就行
    dfs(0)
    return res


if __name__ == "__main__":
    x = [1, 2, 3]
    prt = func(x)
    print(prt)
