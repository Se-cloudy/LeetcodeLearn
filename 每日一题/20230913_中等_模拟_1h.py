#2023.9.13.14:29
#2596. 检查骑士巡视方案

#delta>=3
#实现list遍历 14:49
#封装函数; 类的实例调用；14:57
#测试用例报错;够不着.看题解 重新模拟；15:11;
#range小bug;
# AC: 15:22

from typing import List

class Solution:
    def func(self, grid: List[List[int]]) -> bool:
        res = True
        n = len(grid[0])
        if grid[0][0]!=0:
            return False
        temp = [[] for i in range(n*n)]
        for i in range(n):
            for j in range(n):
                temp[grid[i][j]] = [i,j]
        for k in range(1, len(temp)):
            x1 = temp[k-1][0]
            y1 = temp[k - 1][1]
            x2 = temp[k][0]
            y2 = temp[k][1]
            if abs((x1-x2)*(y1-y2))!=2:
                return False
        return res

grid = [[0,3,6],[5,8,1],[2,7,4]]

t = Solution()
print(t.func(grid))
