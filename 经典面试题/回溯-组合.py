"""
77. 组合
中等
给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
你可以按 任何顺序 返回答案。

示例 1：
输入：n = 4, k = 2
输出：
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

zzl：看来return就是len=k的时候了;自己写出来的本地AC！continue是核心啊
但是没有去除重复的组合。继续改改。应该加begin。
"""
from typing import List


def func(n:int, k: int) -> List[List[int]]:
    res = []
    path = []

    def dfs(begin, path):
        if len(path) == k:
            res.append(path)
            return
        for i in range(begin, n+1): # 去除重复组合; 本问题天然有序啊。
            if path and i == path[-1]:  # 去除重复数字
                continue
            dfs(i, path + [i])


    dfs(1, path)
    return res


if __name__ == "__main__":
    x = 4
    y = 2
    prt = func(x, y)
    print(prt)
