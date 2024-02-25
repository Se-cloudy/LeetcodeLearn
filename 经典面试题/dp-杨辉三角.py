"""
118. 杨辉三角

zzl 这都有点写不对。。
"""
import collections
from typing import List

import numpy as np

def func(numRows: int) -> List[List[int]]:
    res = [[1]*(i+1) for i in range(numRows)]
    if numRows < 3:
        return res
    for i in range(2, numRows):
        for j in range(1, i):  # 注意从1开始
            res[i][j] = res[i-1][j-1]+res[i-1][j]
    return res


if __name__ == "__main__":
    x = 5
    y = 2
    prt = func(x)
    print(prt)
