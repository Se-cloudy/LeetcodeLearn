"""
763. 划分字母区间 中等
给你一个字符串 s 。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。
注意，划分结果需要满足：将所有划分结果按顺序连接，得到的字符串仍然是 s 。
返回一个表示每个字符串片段的长度的列表。

示例 1：
输入：s = "ababcbacadefegdehijhklij"
输出：[9,7,8]
解释：
划分结果为 "ababcbaca"、"defegde"、"hijhklij" 。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 这样的划分是错误的，因为划分的片段数较少。

zzl：做完这道就回去打电话 眼睛疼。中等而已，我一直是中上的捏
记录起始位置信息是必须的准备开销；数据分析是第一步。

存储技巧；双指针；
"""
from typing import List


def func(s: str) -> List[int]:
    res = []
    last = [0] * 26  # 初始化在哪里都是好习惯！
    for i, c in enumerate(s):
        last[ord(c)-ord('a')] = i  # 必须这样写。

    start = end = 0
    for i, c in enumerate(s):
        end = max(last[ord(c)-ord('a')], end)
        if i == end:
            res.append(end-start+1)
            start = end + 1
    return res


if __name__ == "__main__":
    x = "ababcbacadefegdehijhklij"
    y = 4
    prt = func(x)
    print(prt)
