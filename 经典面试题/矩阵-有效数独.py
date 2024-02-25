"""
36. 有效的数独 中等
请你判断一个 9 x 9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。
数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）

注意：
一个有效的数独（部分已被填充）不一定是可解的。只需要根据以上规则，验证已经填入的数字是否有效即可。
空白格用 '.' 表示。
输入：board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
输出：true

zzl.2023.12.19
暴力AC；太不优雅了。。看题解有位运算的 学学。。
"""
from typing import List


def check(ls: List[str]) -> bool:
    cnt = {}
    for i in ls:
        if i == '.':
            pass
        else:
            cnt[i] = cnt.get(i, 0) + 1
            if cnt[i] > 1:
                return False
    return True

def func1(board: List[List[str]]) -> bool:
    res = True
    n = len(board[0])  # 方阵
    # 检验横向
    for i in range(n):
        cur = check(board[i])
        if not cur:
            return False
    # 检验纵向
    for i in range(n):
        temp = [xx[i] for xx in board]
        cur = check(temp)
        if not cur:
            return False
    # 检验区域
    for i in range(0,n,3):
        for j in range(0, n, 3):
            # 拓展
            temp = board[i][j:j+3]
            temp += board[i+1][j:j+3]
            temp += board[i+2][j:j+3]
            cur = check(temp)
            if not cur:
                return False
    return res


def func2(self, board: List[List[str]]) -> bool:
    # 学习；位运算+坐标寻址，tql
    # 9位二进制表示数字，&查询是否已经出现。
    row = [0] * 9
    col = [0] * 9
    box = [0] * 9
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                continue
            num = 1 << int(board[i][j])  # 要熟悉用位运算表示数字，何况还是0-9这么少的
            b = (i // 3) * 3 + j // 3  # 寻址
            if row[i] & num != 0 or col[j] & num != 0 or box[b] & num != 0:
                return False
            row[i] |= num
            col[j] |= num
            box[b] |= num
    return True


if __name__ == "__main__":
    x = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    prt = func1(x)
    print(prt)
