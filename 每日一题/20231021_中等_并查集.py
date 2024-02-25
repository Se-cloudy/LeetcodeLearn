# 抄的 并查集 能理解就好了
# 默写了一遍提交了 能理解 实现起来有class的困难

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for x, y in edges:
            uf.union(x, y)
        res = 0
        for i in range(n):
            res += n - uf.getSize(uf.find(i))
        return res // 2

class UnionFind:
    def __init__(self, n: int):
        self.parents = [i for i in range(n)]  # 初始化父节点为自己
        self.sizes = [1] * n

    def find(self, x: int) -> int:
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x: int, y: int):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            if self.sizes[rx] > self.sizes[ry]:  # 寡不敌众。。
                self.parents[ry] = rx
                self.sizes[rx] += self.sizes[ry]
            else:
                self.parents[rx] = ry
                self.sizes[ry] += self.sizes[rx]

    def getSize(self, x: int) -> int:
        return self.sizes[x]