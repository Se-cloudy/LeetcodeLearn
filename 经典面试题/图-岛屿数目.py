"""
200. 岛屿数量
中等
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。

示例 1：
输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1

zzl：直接学习。第一遍没有AC，infect的检验有效边界没写好。。经典边界细节。
思路：遍历岛这个二维数组，如果当前数为1，则进入感染函数并将岛个数+1
感染函数：递归标注，将所有相连的1都标注成2。这样就避免了遍历过程中的重复计数的情况，一个岛所有的1都变成了2后，遍历的时候就不会重复遍历了。

"""
from typing import List

def infect(grid: List[List[str]], i, j):
    if  i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1:
        return
    if grid[i][j] != "1":
        return
    grid[i][j] = "2"
    infect(grid, i - 1, j)
    infect(grid, i + 1, j)
    infect(grid, i, j - 1)
    infect(grid, i, j + 1)

def func(grid: List[List[str]]) -> int:
    res = 0
    col = len(grid[0])
    row = len(grid)
    for i in range(row):
        for j in range(col):
            if grid[i][j] == "1":
                infect(grid, i, j)
                res += 1
    return res


if __name__ == "__main__":
    x = [
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    prt = func(x)
    print(prt)
