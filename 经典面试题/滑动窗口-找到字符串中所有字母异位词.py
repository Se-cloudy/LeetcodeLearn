"""
438. 找到字符串中所有字母异位词 中等
给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。

示例 1:
输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。

zzl：滑动窗口，返回left数组；
10min 暴力排序，，经典超时。用26位数来表示吧。ok，还是超时
学习滑动窗口；还有特例边界。
"""
import collections
from typing import List


def func(s: str, p: str) -> List[int]:
    res = []
    s_len, p_len = len(s), len(p)
    if s_len < p_len:
        return res
    p_ls = [0] * 26
    for i in p:
        p_ls[ord(i) - ord('a')] += 1  # 有重复 需要加而不是赋等
    s_ls = p_ls.copy()

    if s_ls == p_ls:
        res.append(0)
    for i in range(s_len-p_len):
        s_ls[ord(s[i])-ord('a')] -= 1  # s_ls是一个和p_ls一样的小窗口
        s_ls[ord(s[i+p_len])-ord('a')] += 1  # 移动

        if s_ls == p_ls:
            res.append(i+1)
    return res


if __name__ == "__main__":
    x = "ababababab"
    y = "aab"
    prt = func(x, y)
    print(prt)
