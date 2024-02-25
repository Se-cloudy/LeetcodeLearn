"""
40. 组合总和 II 中等
给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用 一次 。
注意：解集不能包含重复的组合。

示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
输出:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

zzl：什么是重复。
"""
from typing import List


def func(candidates: List[int], target: int) -> List[List[int]]:
    res = []
    n = len(candidates)
    path = []

    def dfs(begin, path, target):
        if target < 0:
            return
        if target == 0:
            res.append(path.copy())
            return  # 回溯到上一层
        for i in range(begin, n):
            if i > begin and candidates[i] == candidates[i-1]:  # 标准去重
                continue
            dfs(i+1, path + [candidates[i]], target - candidates[i])  # 为什么要i+1

    dfs(0, path, target)
    return res


if __name__ == "__main__":
    x = [1,2,3]
    y = 5
    prt = func(x, y)
    print(prt)
