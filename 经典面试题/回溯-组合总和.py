"""
39. 组合总和
中等
给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。
candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。
对于给定的输入，保证和为 target 的不同组合数少于 150 个。

示例 1：
输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
解释：
2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
7 也是一个候选， 7 = 7 。
仅有这两种组合。

zzl：模板的好处逐渐显现。。切记细节。此时用begin而不是visited
排列问题，讲究顺序（即 [2, 2, 3] 与 [2, 3, 2] 视为不同列表时），需要记录哪些数字已经使用过，此时用 used 数组；
组合问题，不讲究顺序（即 [2, 2, 3] 与 [2, 3, 2] 视为相同列表时），需要按照某种顺序搜索，此时使用 begin 变量。
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
            res.append(path)
            return  # 回溯到上一层
        for i in range(begin, n):
            dfs(i, path + [candidates[i]], target - candidates[i])  # 注意path+后面的[]; 注意是不是i+1

    dfs(0, path, target)
    return res

def func1(candidates: List[int], target: int) -> List[List[int]]:
    res = []
    n = len(candidates)
    path = []

    def dfs(begin):
        cur = sum(path)
        if cur == target:
            res.append(path[:])  # 使用 path[:] 创建列表的副本
        elif cur > target:
            return

        for i in range(begin,n):
            path.append(candidates[i])
            dfs(i)  # 这里绝对不能i+1。不然就是不重复选择的组合。
            path.pop()

    dfs(0)
    return res


if __name__ == "__main__":
    x = [2,3,6,7]
    y = 7
    prt = func(x, y)
    print(prt)
